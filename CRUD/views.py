from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import RegisterData

# Create your views here.

#### insert into Tblname values(fname,lname,email,password)
###  RegisterData(first_name="pradip",last_name="pawar",email="pradip@gmail.com",password="123").save()


### select * from tbl_name
### RegisterData.objects.all()


def register(request):

    All_Data = RegisterData.objects.all()

    print("All_Data:====> ",All_Data)

    if request.method == 'POST':
        print("yes===================================================")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(fname,lname,email,password)
        RegisterData(first_name=fname,last_name=lname,email=email,password=password).save()
        return redirect("register")  ####
        

    return render(request,"reg/register.html",{"all_data":All_Data})

# "D:\PRADIP\c4c\djnago\CRUDOPR\templates\reg/register.html"

def login(request):
    return HttpResponse("login")