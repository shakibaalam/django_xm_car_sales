from django.db import models
from django.contrib.auth.models import User
from cars.models import CarModel

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user.username} on {self.car.title}'

