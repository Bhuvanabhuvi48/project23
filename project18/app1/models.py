from django.db import models

# Create your models here.
class Bhuna2(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20,blank=False)
    job=models.CharField(max_length=20,blank=False)
    sal=models.FloatField()
