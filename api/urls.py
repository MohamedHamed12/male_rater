from django.db import router
from django.urls import include, path
from rest_framework import routers

from .views import MealViewsSet,RateViewsSet
router=routers.DefaultRouter()
router.register('meals',MealViewsSet)
router.register('rates',RateViewsSet)
urlpatterns = [
    path('',include(router.urls)),
]
