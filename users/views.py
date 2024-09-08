from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User


def index(req):
    return render(req,"users/index.html")

def insertUser(req):
    data = req.POST
    User(name_text=data['Name'],email_text=data['Email'],password_text=data['Password']).save()


    return render(req,'users/index.html',{"message":"Conta Criada com sucesso!!"})

def LoginUser(req):
    data = req.POST
    try:
        login = User.objects.get(email_text = data['Email'],password_text = data['Password'])
        url = "/tasks/"+str(login.id)
        return redirect(url)
    except:
        return render(req,'users/index.html',{"message":"Email ou Senha ou incorretos"})

# Create your views here.
