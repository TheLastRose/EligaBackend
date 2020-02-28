from rest_framework import viewsets
from .models import *
from .serializers import *


class ProductbacklogViewSet(viewsets.ModelViewSet):
    queryset = product_backlog.objects.all()
    serializer_class =  ProductbacklogSerializer
    filter_fields = ('sprintID',)

# class SprintViewSet(viewsets.ModelViewSet):
#     queryset = sprint.objects.all()
#     serializer_class =  SprintSerializer

class SprintbacklogViewSet(viewsets.ModelViewSet):
    queryset = sprint_backlog.objects.all()
    serializer_class =  SprintbacklogSerializer
    filter_fields = ('sprintID',)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = task_model.objects.all()
    serializer_class =  TaskSerializer
    filter_fields = ('sprintbacklogID',)

class UserViewSet(viewsets.ModelViewSet):
    queryset = user_model.objects.all()
    serializer_class =  UserSerializer
    filter_fields = ('id',)