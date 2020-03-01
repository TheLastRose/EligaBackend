from django.db import models
import datetime

# Create your models here.
class product_backlog(models.Model):
    sprintbacklogID   = models.PositiveIntegerField(default= 0)
    content           = models.TextField()
    priority          = models.CharField(max_length=5)
    hours             = models.PositiveIntegerField()
    dateCreated       = models.DateTimeField(auto_now=True)

class sprint_backlog(models.Model):
    startDate         = models.DateField(default=datetime.date.today)
    dueDate           = models.DateField(default=datetime.date.today)
    name              = models.TextField(default= 'Sprint Name')

class task_model(models.Model):
    sprintbacklogID     = models.PositiveIntegerField(default= 0)
    productbacklogID    = models.PositiveIntegerField(default= 0)
    content             = models.TextField()
    assignTo            = models.PositiveIntegerField(default= 0)
    assignToName        = models.CharField(max_length=15,default='Name of User')
    dateCompleted       = models.DateField(blank=True) #Remember set =null in DB
    hours               = models.PositiveIntegerField(default= 0)
    status              = models.CharField(max_length=10, default= 'Incomplete')
    dateCreated         = models.DateTimeField(auto_now=True)

class user_model(models.Model):
    name        = models.CharField(max_length=15,default='Name of User')
    role        = models.CharField(max_length=15,default='User Role')
    dateCreated = models.DateTimeField(auto_now=True)
    #name, role, avatar