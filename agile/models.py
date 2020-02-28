from django.db import models

# Create your models here.
class product_backlog(models.Model):
    sprintbacklogID   = models.PositiveIntegerField(default= 0)
    content           = models.TextField()
    priority          = models.CharField(max_length=5)
    hours             = models.PositiveIntegerField()
    dateCreated       = models.DateTimeField(auto_now=True)

class sprint_backlog(models.Model):
    startDate         = models.DateField()
    dueDate           = models.DateField()
    content           = models.TextField(default= ' ')
    name              = models.TextField(default= 'Sprint Name')

# class sprint_backlog(models.Model):
#     sprintID            = models.PositiveIntegerField()
#     content             = models.TextField()
#     dateCreated         = models.DateTimeField(auto_now=True)

class task_model(models.Model):
    sprintbacklogID     = models.PositiveIntegerField(default= 0)
    productbacklogID    = models.PositiveIntegerField(default= 0)
    content             = models.TextField()
    assignTo            = models.PositiveIntegerField(default= 0)
    dateCompleted       = models.DateField(auto_now=True)
    hours               = models.PositiveIntegerField(default= 0)
    status              = models.CharField(max_length=10)
    dateCreated         = models.DateTimeField(auto_now=True)

# class task_status(models.Model):
#     date        = models.DateField()
#     totalTasks  = models.PositiveIntegerField()
#     remainTasks = models.PositiveIntegerField()

class user_model(models.Model):
    name        = models.CharField(max_length=15,default='Name of User')
    role        = models.CharField(max_length=15,default='User Role')
    dateCreated = models.DateTimeField(auto_now=True)
    #name, role, avatar