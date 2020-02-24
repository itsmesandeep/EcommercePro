from django.shortcuts import render,redirect
from .models import RegistrationsData
from django.http import HttpResponse


def registrationView(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        if pwd!=cpwd:
            return HttpResponse('<h1> PleaseCheck Password </h1>')
        mobile = request.POST.get('mobile')
        emailid = request.POST.get('emailid')
        data = RegistrationsData(
            uname=uname,
            password=pwd,
            mobileNo=mobile,
            emailId=emailid
        )
        data.save()
        return HttpResponse('<h1> Details Saved Succesfully</h1>')

    else:
        return render(request,'ecomm/registration.html')

def loginView(request):
    if request.method =="POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        vaildCradentials = RegistrationsData.objects.filter(uname=uname,password=pwd)
        if not vaildCradentials:
            return HttpResponse('<h1> Not a Vaild User</h1>')
        else:
            return HttpResponse('<h1>  Vaild User</h1>')
    else:
        return render(request,'ecomm/login.html')


def updatePassword(request):
    if request.method=="POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        if pwd!=cpwd:
            return HttpResponse('<h1>Password Miss Match Please </h1>')
        else:
            udata = RegistrationsData.objects.filter(uname=uname)
            udata.update(password = pwd)
            return HttpResponse('<h1>Password Modified</h1>')



    else:
        return render(request, 'ecomm/updatePwd.html')


def resetPassword(request):
    if request.method =="POST":
        email = request.POST.get('email')
        emailFound = RegistrationsData.objects.filter(emailId=email)
        if emailFound:
            return redirect('updatepassword')
        else:
            return HttpResponse('<h1>Email Not Found</h1>')
    else:
        return  render(request,'ecomm/resetPassword.html')


def productsView(request):
    return render(request,'ecomm/productPages.html')