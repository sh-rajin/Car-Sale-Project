
from django import forms
from .models import CarBrandModel


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrandModel
        fields = '__all__'

