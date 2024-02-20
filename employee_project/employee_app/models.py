from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    salary = models.FloatField()
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)