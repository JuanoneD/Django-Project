from django.db import models

# Create your models here.
class User(models.Model):
    name_text = models.CharField(max_length=200)
    email_text = models.CharField(max_length=200)
    password_text = models.CharField(max_length=200)

    def __str__(self):
        return 'name:'+ self.name_text + ' Email:' + self.email_text
