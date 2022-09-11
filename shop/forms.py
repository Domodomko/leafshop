from .models import Order
from django import forms


class OrderShippingForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('email', 'shipping_first_name', 'shipping_last_name', 'shipping_address', 'shipping_city',
                  'shipping_province', 'shipping_postal', 'shipping_phone')


class OrderPaymentForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('billing_first_name', 'billing_last_name', 'billing_address', 'billing_city',
                  'billing_province', 'billing_postal', 'billing_phone')
