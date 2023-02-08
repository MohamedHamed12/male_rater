from turtle import title
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
User =settings.AUTH_USER_MODEL


class Meal(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.title)
class Rate(models.Model):
    meal=models.ForeignKey(Meal, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together=(('user', 'meal'))
        index_together=(('user', 'meal'))
    def __str__(self) :
        return str(self.meal)+ "-"+str(self.user)