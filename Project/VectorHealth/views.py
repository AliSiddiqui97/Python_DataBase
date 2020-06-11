
from django.shortcuts import render, redirect
import os
import pandas as pd
import BI_DB
def home(request):
    return render(request,'home.html')

def scriptDrive(request):
    print(os.getcwd())
    
    os.system("python Script.py")
    
    from_dest = {"From":"DRIVE"}
    
    return render(request,"displayDrive.html",from_dest)


def scriptMail(request):
    print(os.getcwd())
    from_dest = {"From":"MAIL"}
    os.system("python Email_Script.py")
    return render(request,"displayDrive.html",from_dest)

    
def readFile(request):

    search = request.POST.get('search')
    opt = request.POST.get('sel')
    option = str(opt).split('-')
    BI_DB.main(option[0],str(search))
    # str_prg ="python BI_DB.py "+option[0]+' '+str(search)
    
    # os.system(str_prg)

    return render(request,"readFiles.html")