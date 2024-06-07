from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cars.models import CarModel
from .models import OrderModel

@login_required
def buy_car(request, pk):
    car = get_object_or_404(CarModel, pk=pk)
    if car.quantity > 0:
        OrderModel.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
    return redirect('profile')
