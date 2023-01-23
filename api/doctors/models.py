from django.db import models
from django.contrib.auth.models import User

class Stakeholder(models.Model):
    class Meta:
        verbose_name = "Stakeholders"

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    


    def __str__(self):
        return "{:s} {:s}".format(self.first_name, self.last_name)



class Employees(models.Model):
    pass