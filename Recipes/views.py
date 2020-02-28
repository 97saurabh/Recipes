from django.shortcuts import render
# Create your views here.

from django.http import HttpResponseRedirect
from django.views.generic import View,UpdateView
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect

from . import forms,models

def food_create(request):
    registered = False
    if request.method == "POST":
        user_form = forms.FoodForm(data=request.POST)
        if user_form.is_valid():
            use = user_form.save(commit=False)

            #use.save()
            use.user=request.user
            if 'profile_pic' in request.FILES:
                use.profile_pic = request.FILES['profile_pic']
            use.save()

            registered = True
            return redirect(reverse_lazy('home'))
        else:
            print(user_form.errors)
    else:

        user_form =forms.FoodForm()
    return render(request,'file_upload.html',{
                                    'user_form':user_form,
                                    'registered':registered,
    })
class LocationUpdateView(UpdateView):
    model = models.Food
    template_name = 'food_update.html'
    form_class = forms.FoodFormUpdate
    success_url = reverse_lazy('home')



def food_detail(request,pk):
    a=models.Food.objects.get(pk=pk)


    return render(request,'food_detail.html',{
                                    'a':a,
    })
def about_me(request):



    return render(request,'about_me.html',{})
from django.db.models import Q
def search(request):
    if request.method=="POST":
        srch=request.POST['srh']
        if srch:
            match=models.Food.objects.filter(Q(food_name__icontains=srch)|
                                             Q(food_in__icontains=srch)
                                             )
            if match:
                print("Hell")
                return render(request,'search.html',{'data':match,})
            else:
                return render(request,'search.html',{'da':"Oops! Recipe Not Matched",})
        else:
            return HttpResponseRedirect(reverse('home'))

    return HttpResponseRedirect(reverse('home'))
