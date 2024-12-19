

from django.shortcuts import render,redirect
from car_app.models import CarModel
from brands.models import CarBrandModel
from django.contrib import messages
# Create your views here.

def home(request, brand_slug=None):
    brands = CarBrandModel.objects.all()
    if not brand_slug == None:
        brand = CarBrandModel.objects.get(slug=brand_slug)
        data = CarModel.objects.filter(brand=brand)
        return render(request, 'home.html',{'data':data, 'brand':brands})
    else:
        data = CarModel.objects.all()
        return render(request, 'home.html', {'brand': brands, 'data': data})



    
def buy_now(request, id):
    if request.user.is_authenticated:
        car = CarModel.objects.get(id=id)
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            messages.success(request, f'You have purchased {car.name}')
        else:
            messages.warning(request, 'This car is out of stock')

        return redirect('homepage')