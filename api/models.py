from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
User =settings.AUTH_USER_MODEL


class Meal(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=200)


    
    def no_of_ratings(self):
        return len( Rate.objects.filter(meal=self)) 

    def avg_ratings(self):
        sum_rates=0
        meal_ratings=Rate.objects.filter(meal=self)
        for rate in meal_ratings:
            sum_rates += rate.stars
        if len(meal_ratings)>0 :return sum_rates/len(meal_ratings)
        return 0

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