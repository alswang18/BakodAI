from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import json
img_height, img_width=128,128
classes=['agriculture','artisinal_mine','bare_ground','blooming','blow_down','clear',
'cloudy','conventional_mine','cultivation','habitation','haze',
'partly_cloudy','primary','road','selective_logging','slash_burn','water']

def index(request):
    context={'a':1}
    return render(request, 'upload.html', context)

def predictImage(request):
    print(request.POST.dict())
    print(request.FILES['filePath'])

    fileObj= request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    context={'filePathName':filePathName,'predictedLabel':predictedLabel}
    return render(request, 'upload.html', context)

def viewDataBase(request):
    import os
    listOfImages=os.listdir('./media/')
    listOfImagesPath=['./media/'+i for i in listOfImages]
    context={'listOfImagesPath':listOfImagesPath}
    return render(request,'viewDB.html',context) 