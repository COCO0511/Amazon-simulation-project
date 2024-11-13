from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Cart

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        
        products = kwargs.pop('products', Product.objects.all())
        
        super(CartForm, self).__init__(*args, **kwargs)
        # all_products = Product.objects.all()
        self.products = {} 
        for product in products:
        # for product in all_products:
            field_name = product.name + " $" + str(product.price)
            self.fields[field_name] = forms.IntegerField(initial=0, min_value=0,
                                                         widget=forms.NumberInput(attrs={'class': 'form-control'}))
            self.products[field_name] = product

    def save(self, user):
        for field_name, product in self.products.items():
            quantity = self.cleaned_data.get(field_name)
            if quantity > 0:
                cart_item, created = Cart.objects.get_or_create(
                    account=user,
                    product=product,
                    defaults={'quantity': quantity}
                )
                if not created:
                    cart_item.quantity += quantity
                    cart_item.save()
                    
class QueryOrderForm(forms.Form):
    
    order_id = forms.IntegerField()

    def save(self):
        order_id = self.cleaned_data.get("order_id")
        return order_id


class ChangeDestinationForm(forms.Form):
    order_id = forms.IntegerField()
    new_x = forms.IntegerField()
    new_y = forms.IntegerField()

    def save(self):
        order_id = self.cleaned_data.get("order_id")
        new_x = self.cleaned_data.get("new_x")
        new_y = self.cleaned_data.get("new_y")
        return order_id, new_x, new_y
    
