from django.urls import path
from .views import CarListView, CarDetailView

urlpatterns = [
    path('', CarListView.as_view(), name='home'),
    path('brand/<slug:brand_slug>/', CarListView.as_view(), name='brand_wise_post'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
]
