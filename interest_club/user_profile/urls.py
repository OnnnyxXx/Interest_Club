from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.profile, name='profile'),
    path('user_home/', views.User_View, name='user_home'),
    path('posts/create/', views.create_post, name='posts_create'),
    path('profile_user/<int:id>/', views.user_profile, name='user_profile'),

]
