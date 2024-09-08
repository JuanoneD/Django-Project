from django.db import models
from users.models import User

# Create your models here.
class Task(models.Model):
    title_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)
    status_text = models.CharField(max_length=200,default='Pendente')
    userMaker = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userMaker')
    userAssign = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userAssign',null=True)

    def __str__(self):
        return 'name:'+ self.title_text+ ' Status:' + self.status_text + 'by user:'+ self.userMaker.__str__()