from django.db import models

# Create your models here.
class employee(models.Model):
    ename=models.CharField(max_length=20)
    eno=models.IntegerField()
    esal=models.IntegerField()
    ecity=models.CharField(max_length=20)
