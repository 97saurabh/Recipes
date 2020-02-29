from django.shortcuts import render

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import View,UpdateView
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms,models
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
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
class LocationUpdateView(UpdateView,LoginRequiredMixin):
    model = models.Food
    template_name = 'food_update.html'
    form_class = forms.FoodFormUpdate
    success_url = reverse_lazy('home')


@login_required
def food_detail(request,pk):
    a=models.Food.objects.get(pk=pk)


    return render(request,'food_detail.html',{
                                    'a':a,
    })
def about_me(request):



    return render(request,'about_me.html',{})

@login_required
def search(request):
    if request.method=="POST":
        srch=request.POST['srh']
        if srch:
            match=models.Food.objects.filter(Q(food_name__icontains=srch)|
                                             Q(food_in__icontains=srch)
                                             )
            if match:
                
                return render(request,'search.html',{'data':match,})
            else:
                return render(request,'search.html',{'da':"Oops! Recipe Not Matched",})
        else:
            return HttpResponseRedirect(reverse('home'))

    return HttpResponseRedirect(reverse('home'))
