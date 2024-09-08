# Generated by Django 5.1.1 on 2024-09-08 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='userAssign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userAssign', to='users.user'),
        ),
    ]
