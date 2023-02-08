from django.conf import settings
from django.shortcuts import render

from rest_framework import viewsets
from .serializers import  MealSerializer,RatingSerializer
from .models import Meal ,Rate
User =settings.AUTH_USER_MODEL
# class UserViewsSet(viewsets.ModelViewSet):
#     serializer_class=UserSerializer
#     queryset=User

class MealViewsSet(viewsets.ModelViewSet):
    serializer_class=MealSerializer
    queryset=Meal.objects.all()


class RateViewsSet(viewsets.ModelViewSet):
    serializer_class=RatingSerializer
    queryset=Rate.objects.all()