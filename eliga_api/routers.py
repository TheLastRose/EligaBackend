from rest_framework import routers
from agile.viewsets import *


router = routers.DefaultRouter()
router.register(r'productbacklog', ProductbacklogViewSet)
router.register(r'sprintbacklog', SprintbacklogViewSet)
router.register(r'task', TaskViewSet)
router.register(r'user', UserViewSet)