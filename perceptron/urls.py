from django.urls import path
from . import views

urlpatterns = [
    path('perceptron/', views.vista_perceptron, name='perceptron'),
    path('', views.vista_perceptron, name='home'), 
]