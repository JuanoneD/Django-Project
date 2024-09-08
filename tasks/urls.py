from django.urls import path
from . import views


app_name = "tasks"

urlpatterns = [

    path('<int:id_user>',views.index,name='index'),
    path('/<int:id_user>/insertTask',views.insertTask,name='insertTask'),
    path('<int:id_user>/<int:id_task>/updateTask',views.updateTask,name="updateTask"),
    path('<int:id_task>/deleteTask',views.deleteTask,name="deleteTask")

]