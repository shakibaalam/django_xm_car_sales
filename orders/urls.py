from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:pk>/', views.buy_car, name='buy_car'),
]
