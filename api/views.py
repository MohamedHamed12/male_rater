import email
from urllib import response
from django.conf import settings
from django.shortcuts import render

from rest_framework import viewsets ,status
from .serializers import  MealSerializer,RatingSerializer
from .models import Meal ,Rate
from rest_framework.decorators import action,api_view
from rest_framework.response import Response 
from api import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
# class UserViewsSet(viewsets.ModelViewSet):
#     serializer_class=UserSerializer
#     queryset=User

class MealViewsSet(viewsets.ModelViewSet):
    serializer_class=MealSerializer
    queryset=Meal.objects.all()

    @action(detail=True, methods=['post'])
    def rate_meal(self,req,pk=None):
        try:
            newstars=req.GET.get('stars')
            meal=Meal.objects.get(id=pk)
          
            email=req.GET.get('email')
            
            user=User.objects.get(email=email)
            print(user.email)
            try:
                # update the current rating 
                rating =Rate.objects.get(meal=meal, user=user)
                rating.stars=newstars
                rating.save()
                serializer=RatingSerializer(rating,many=False)
                json={
                    "massage":"updated me",
                    "result":serializer.data,
                }
                return Response(json,status=status.HTTP_200_OK)
            except :
                rating =Rate.objects.create(meal=meal, user=user,stars=newstars)
                serializer=RatingSerializer(rating,many=False)
                json={
                    "massage":"inserted into me ",
                    "result":serializer.data,
                }
                return Response(json,status=status.HTTP_200_OK)
               
               
                # insert a new rating 
        except :
            json={
                    "massage":"this BAD_REQUEST me",
                    
                }
            return Response(json,status=status.HTTP_400_BAD_REQUEST)






class RateViewsSet(viewsets.ModelViewSet):
    serializer_class=RatingSerializer
    queryset=Rate.objects.all()