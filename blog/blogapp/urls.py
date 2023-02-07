from django.urls import path
from blogapp import views
from blogapp.views import *
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/', views.post, name='post'),
    path('post-details/<pk>', views.post_details, name='post_details'),
    path('login/', views.usrLogin, name='login'),
    path("logout/", views.usrLogout, name='logout'),
    path('register/', views.register, name='register'),
    path('post-upload/', views.post_uploader, name='post-upload'),
    path('profile/', views.profile, name='profile'),
    path('profile/profile-edit/', views.edit_profile, name="profile-edit"),
    path('post-edit/<pk>', views.edit_post, name='edit_post'),
    path('/delete-post/<pk>', views.delete_post, name='delete_post'),
    
]