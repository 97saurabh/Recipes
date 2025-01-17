from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'basicapp'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
