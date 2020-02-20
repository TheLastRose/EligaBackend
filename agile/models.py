from django.db import models

# Create your models here.
class product_backlog(models.Model):
    #backlogID   = models.AutoField(primary_key=True)
    sprintID          = models.PositiveIntegerField(default= 0)
    content           = models.TextField()
    priority          = models.CharField(max_length=5)
    hours             = models.PositiveIntegerField()
    dateCreated       = models.DateTimeField(auto_now=True)

class sprint_backlog(models.Model):
    sprintID            = models.PositiveIntegerField()
    content             = models.TextField()
    dateCreated         = models.DateTimeField(auto_now=True)

class sprint(models.Model):
    startDate         = models.DateField()
    dueDate           = models.DateField()

class task_model(models.Model):
    sprintbacklogID     = models.PositiveIntegerField()
    content             = models.TextField()
    assignTo            = models.PositiveIntegerField()
    status              = models.PositiveIntegerField()
    dateCreated         = models.DateTimeField(auto_now=True)

class user_model(models.Model):
    username    = models.CharField(max_length=25)
    password    = models.CharField(max_length=25)
    dateCreated = models.DateTimeField(auto_now=True)