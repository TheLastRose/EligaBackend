from rest_framework import serializers
from .models import *


class ProductbacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_backlog
        fields = '__all__'
class SprintbacklogSerializer(serializers.ModelSerializer):
    class Meta:
        model = sprint_backlog
        fields = '__all__'
class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = sprint
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_model
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'