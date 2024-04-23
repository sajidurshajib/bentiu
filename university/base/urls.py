from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('cources/', views.cources, name='cources'),
    path('contact/', views.contacts, name='contact'),
]