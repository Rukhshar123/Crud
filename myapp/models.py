from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=12)
