
from django.forms import ModelForm

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'bag',
            'email',
            'collection_date'
        ]