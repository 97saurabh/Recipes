from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'recipes'
urlpatterns = [
    path('create/',views.food_create,name='food_create'),
    re_path(r'^food/(?P<pk>\d+)/update/$',views.LocationUpdateView.as_view(),name='food_update'),
    re_path(r'^food/(?P<pk>\d+)/detail/$',views.food_detail,name='food_detail'),
    path('about_me/',views.about_me,name='about_me'),
    path('search/',views.search,name="search"),


]
