from django.shortcuts import render,get_object_or_404,redirect
from users.models import User
from .models import Task
from django.db.models import Q

# Create your views here.
def index(req,id_user):
    user = get_object_or_404(User,pk=id_user)
    filter = 0

    if req.POST and  req.POST['filter'] != "all":
        tasks = Task.objects.filter(Q(userMaker = user)|Q(userAssign = user),Q(status_text = req.POST['filter']))
        if req.POST['filter'] == "Em andamento":
            filter = 1
        elif req.POST['filter'] == "Pendente":
            filter = 2
        else:
            filter = 3

    else:
        tasks = Task.objects.filter(Q(userMaker = user)|Q(userAssign = user))

    print(filter)
    return render(req,"tasks/index.html",{"user":user,"tasks":tasks,'filter':filter})

def insertTask(req,id_user):
    user = get_object_or_404(User,pk=id_user)
    data = req.POST
    try:
        user_assign = User.objects.get(email_text = data['Email'])
        Task(title_text=data['Title'],description_text=data['Description'],userMaker = user,userAssign = user_assign).save() 
        # não cria se não ouver user assing
    except: 
        Task(title_text=data['Title'],description_text=data['Description'],userMaker = user).save()

    return redirect("/tasks/"+str(user.id))

def updateTask(req,id_user,id_task):
    data = req.POST
    task = get_object_or_404(Task,pk=id_task)
    task.title_text = data['Title']
    task.description_text=data['Description']
    task.status_text = data['Status']
    try:
        user_assign = User.objects.get(email_text = data['Email'])
        task.userAssign = user_assign
        task.save()
    except:
        task.save()

    return redirect("/tasks/"+str(id_user))

def deleteTask(req,id_task):
    task = get_object_or_404(Task,pk=id_task)
    id_user = str(task.userMaker.id)
    task.delete()
    return redirect("/tasks/"+str(id_user))

