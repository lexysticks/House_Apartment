from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('rebt',views.rent,name='rent'),
    path('buy',views.buy,name='buy'),
    path('shortlet',views.short,name='shortlet'),
    path('land',views.land,name='land'),
    path('contact',views.contact,name='contact')
]