# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    shopName = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    class Meta(AbstractUser.Meta):
        pass

class Component(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
       return self.name

class DeviceModel(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
       return self.name

class Device(models.Model):
    device_model = models.ForeignKey(DeviceModel)
    component_working = models.ManyToManyField('Component', related_name='work+')
    component_not_working = models.ManyToManyField('Component', related_name='notwork+')
    def __unicode__(self):
       return self.device_model

class Solution(models.Model):
    component = models.ForeignKey(Component)
    solution = models.CharField(max_length=200,blank=True)
    def __unicode__(self):
       return self.component