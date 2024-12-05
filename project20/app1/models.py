from django.db import models

# Create your models here.emp
class Employers(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    sal=models.IntegerField()