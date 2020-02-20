from rest_framework import viewsets
from .models import *
from .serializers import *


class ProductbacklogViewSet(viewsets.ModelViewSet):
    queryset = product_backlog.objects.all()
    serializer_class =  ProductbacklogSerializer

class SprintViewSet(viewsets.ModelViewSet):
    queryset = sprint.objects.all()
    serializer_class =  SprintSerializer
    
class SprintbacklogViewSet(viewsets.ModelViewSet):
    queryset = sprint_backlog.objects.all()
    serializer_class =  SprintbacklogSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = task_model.objects.all()
    serializer_class =  TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = user_model.objects.all()
    serializer_class =  UserSerializer