from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):
    user=models.ForeignKey('auth.User',on_delete='CASCADE',related_name='foods',blank=True)
    food_name=models.CharField(max_length=25,blank=False)
    food_des=models.TextField(max_length=1000)
    food_in=models.CharField(max_length=25)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def get_absolute_url(self):
        return reverse('home')
    def __str__(self):
        return self.food_name
