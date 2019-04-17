# -*- coding: utf-8 -*-
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    detail = models.TextField()
    status = models.CharField(max_length=15)
    priority = models.IntegerField()
    type = models.CharField(max_length=50)
    def __unicode__(self):
        description_string = "{"
        description_string += "name: "+self.name + ","
        description_string += "detail: "+self.detail + ","
        description_string += "status: "+self.status + ","
        description_string += "prio: "+str(self.priority) + ","
        description_string += "type: "+self.type + ""
        description_string += "}"
        return description_string
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    login = models.CharField(max_length=200) #第三方登录信息
    def __unicode__(self):
        description_string = "{"
        description_string += "username: "+self.username + ","
        description_string += "password: "+self.password + ","
        description_string += "phone: "+self.phone + ","
        description_string += "login: "+self.login + ""
        description_string += "}"
        return description_string
