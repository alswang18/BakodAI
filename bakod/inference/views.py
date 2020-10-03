from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import json
img_height, img_width= 128,128
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

    context={'filePathName':filePathName}
    return render(request, 'upload.html', context)