

from django.db import models
from brands.models import CarBrandModel
# Create your models here.


class CarModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(CarBrandModel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/')
    
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.name}'
