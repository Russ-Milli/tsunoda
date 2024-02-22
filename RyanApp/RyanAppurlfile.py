from django.urls import path
from RyanApp import views


urlpatterns = [
  path('welcome/', views.karibu),
  path('', views.homepage, name='My_index'),
  path('about/', views.about, name='My_about'),
  path('personal/', views.personal, name='My_Personal'),
  path('login/', views.login, name='My_Login'),
  path('contact/', views.contact, name='My_Contact'),
  path('services/', views.services, name='My_Services'),
  path('gallery/', views.gallery, name='My_gallery')




]

