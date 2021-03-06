from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.autograd import Variable
import torchvision.models as models

resnet18 = models.resnet18()

classes=['agriculture','artisinal_mine','bare_ground','blooming','blow_down','clear',
'cloudy','conventional_mine','cultivation','habitation','haze',
'partly_cloudy','primary','road','selective_logging','slash_burn','water']

class Flatten(nn.Module):
    "Flatten `x` to a single dimension, often used at the end of a model. `full` for rank-1 tensor"
    def __init__(self, full:bool=False):
        super().__init__()
        self.full = full

    def forward(self, x):
        return x.view(-1) if self.full else x.view(x.size(0), -1)

class AdaptiveConcatPool2d(nn.Module):
	def __init__(self, sz=None):
		super().__init__()
		sz = sz or (1)
		self.ap = nn.AdaptiveAvgPool2d(sz)
		self.mp = nn.AdaptiveMaxPool2d(sz)

	def forward(self, x): return torch.cat([self.mp(x), self.ap(x)], 1)
    
def myhead(nf, nc):
    return \
    nn.Sequential(        # the dropout is needed otherwise you cannot load the weights
            AdaptiveConcatPool2d(),
            Flatten(full=False),
            nn.BatchNorm1d(1024),
            nn.Dropout(p=0.25),
            nn.Linear(1024, 512, bias = False),
            nn.ReLU(True),
            nn.BatchNorm1d(512),
            nn.Dropout(p=0.5),
            nn.Linear(512, nc,bias = False),
        )

my_model=models.resnet18() 
modules=list(my_model.children())
modules.pop(-1) 
modules.pop(-1) 
temp=nn.Sequential(nn.Sequential(*modules))
tempchildren=list(temp.children()) 
tempchildren.append(myhead(512,17))
my_r18=nn.Sequential(*tempchildren)

model=my_r18
weighties = torch.load('model/fastai-rn18.pth',map_location=torch.device('cpu'))
model.load_state_dict(weighties['state_dict'])
model.eval()

import json
img_height, img_width=128,128
classes=['agriculture','artisinal_mine','bare_ground','blooming','blow_down','clear',
'cloudy','conventional_mine','cultivation','habitation','haze',
'partly_cloudy','primary','road','selective_logging','slash_burn','water']

def index(request):
    if request.method == 'POST' and request.FILES['filePath']:
        print(request.POST.dict())
        print(request.FILES['filePath'])

        fileObj= request.FILES['filePath']
        fs = FileSystemStorage()
        filePathName=fs.save(fileObj.name,fileObj)
        filePathNameURL=fs.url(filePathName)
        testimage='.'+filePathNameURL
        from PIL import Image
        imgplanet = Image.open(testimage).convert('RGB')
        preprocess = transforms.Compose([
                transforms.Resize(128),
                transforms.CenterCrop(128),
                transforms.ToTensor(),
                transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )])
        imgplanet_preprocessed = preprocess(imgplanet)
        imgplanet_tensor = torch.unsqueeze(imgplanet_preprocessed, 0)
        tensor_list= model.forward(imgplanet_tensor)
        tensor_list.tolist()
        tensor_list.tolist()[0]
        tensor_tolist = tensor_list.tolist()[0]
        indx = [i for i in range(len(tensor_tolist)) if tensor_tolist[i]>0]
        predictions = [classes[i] for i in indx ]
        context={'filePathName':filePathNameURL,'predictedLabel':predictions}
        return render(request, 'upload.html', context)
    return render(request, 'upload.html')

def viewDataBase(request):
    import os
    listOfImages=os.listdir('./media/')
    listOfImagesPath=['./media/'+i for i in listOfImages]
    context={'listOfImagesPath':listOfImagesPath}
    return render(request,'viewDB.html',context) 