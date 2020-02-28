from django.shortcuts import render

from django.views.generic import TemplateView
from Recipes import models

def home(request):
    data = models.Food.objects.all()
    return render(request,'index.html',{'data':data,})
