from django.db import models

class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.car.title}'

