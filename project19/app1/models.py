from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    sal=models.FloatField()
def __str__(self):
    return f'{self.empno},{self.ename},{self.job},{self.sal}'    
