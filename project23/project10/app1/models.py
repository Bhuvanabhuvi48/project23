from django.db import models

# Create your models here.
class Emp(models.Model):
    empno=models.Model.Integer()
    ename=models.Model.CharField()
    job=models.Model.CharField()
