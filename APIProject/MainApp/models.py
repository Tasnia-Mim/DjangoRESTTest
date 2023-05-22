from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    id = models.IntegerField(auto_created='False', primary_key='True')
    cpm_name = models.CharField(max_length=100, unique=False, blank=False)


class Employee(models.Model):
    id = models.IntegerField(auto_created='False', primary_key='True')
    user = models.CharField(max_length=100, unique=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee', null='True')



class Device(models.Model):
    id = models.IntegerField(auto_created='False', primary_key='True')
    device_type = models.CharField(max_length=100, null='True', blank='True')
    device_model = models.CharField(max_length=100, null='True', blank='True')



class Device_Assignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null='True', blank='True')
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_to', null='True', blank='True')
    assigned_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_by', null='True', blank='True')


