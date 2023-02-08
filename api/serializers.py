from .models import  Meal ,Rate
from rest_framework import serializers

from django.conf import settings
User =settings.AUTH_USER_MODEL

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','email', 'password']
#         extra_Kwargs={'password':{'write_only':True,"required":True}}

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields = ('id', 'title', 'description','price')
    
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'stars', 'user', 'meal')