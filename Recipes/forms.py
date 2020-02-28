from django import forms
from django.contrib.auth.models import User
from .models import Food




class FoodForm(forms.ModelForm):
    class Meta():
        model=Food
        fields = ('food_name','food_des','food_in','profile_pic')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['food_name'].label = 'Recipe Name'
        self.fields['food_des'].label = "Description"
        self.fields['food_in'].label = "Ingredients"
        self.fields['profile_pic'].label = "Upload Photo"


class FoodFormUpdate(forms.ModelForm):
    class Meta():
        model=Food
        fields = ('food_name','food_des','food_in')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['food_name'].label = 'Recipe Name'
        self.fields['food_des'].label = "Description"
        self.fields['food_in'].label = "Ingredients"
