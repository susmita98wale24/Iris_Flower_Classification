from django.urls import path
from . import views

urlpatterns =[
    path('', views.predict_species, name='predict_species'),
]