from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import  *
from datetime import datetime
import requests


def homepage(request):
    return render(request, "Amazon/homepage.html")

def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account Created for {username}. You can now log in")
            
            return redirect("login")
    else:   
        form = UserRegistrationForm()
        
    return render(request, "Amazon/user_register.html", {"form": form})

    

@login_required
def product_list(request):
    
    search_query = request.GET.get('search_query', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.all()
    
    form = CartForm(products=products)
    
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            
            form.save(request.user)
            
            messages.success(request, f"Successfully added to cart.")
            
            return redirect("homepage")
    else:   
        form = CartForm()
        
    return render(request, "Amazon/product_list.html", {"form": form, "search_query": search_query})



@login_required
def cart(request):
    # Retrieve the user's cart
    user = request.user
    
    result = Cart.objects.filter(account=user)
    
    cart = {}

    # Iterate over each item in the cart
    for row in result:
        product_id = row.product_id
        quantity = row.quantity
        product = Product.objects.get(id=product_id)
        product_name = product.name
        product_price = product.price
        subtotal = product_price * quantity
        cart[product_name] = {
            'quantity': quantity,
            'price': product_price,
            'subtotal': subtotal
        }
        
    context = {
        'cart': cart
    }
    
    return render(request, 'Amazon/cart.html', context)

def submit_order(request):
    
    ups_account = request.POST.get('ups_account', None)
    dest_x = request.POST.get('destination_x', None)
    dest_y = request.POST.get('destination_y', None)
    
    # Find the cart associated with the request.user
    cart = Cart.objects.filter(account=request.user)
    
    # Create entry in the Order table
    new_order = Order(amazon_account=request.user, 
                      truck_id=None,
                      ups_account=ups_account,
                      status="processing",
                      destination_x=dest_x,
                      destination_y=dest_y,
                      warehouse=None,
                      price=0,
                      time_created=datetime.now(),
                      time_packed=None,
                      time_loaded=None,
                      time_delivered=None,
                      )
    new_order.save()
    
     # Create entry in the Package table
    for item in cart:
        new_package = Package(order=new_order, product=item.product, quantity=item.quantity)
        new_package.save()
        
        new_order.price += item.product.price * item.quantity
                        
    context = {
        'order_id': new_order .id
    }
    
    cart.delete()
    
    data = {'order_id': new_order.id}
    response = requests.post('http://server:5000/buy', json=data)
    print("Response", response)
    if response.status_code == 200:
        print('Buy Order Response:', response.json())
    
    return render(request, 'Amazon/order_success.html', context)


def query_order(request):
    if request.method == "POST":
        form = QueryOrderForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data.get("order_id")
            order_exists = Order.objects.filter(id=order_id).exists()
            if not order_exists:
                messages.error(request, f"Order ID does not exist!")  # Add an error message
                return render(request, "Amazon/query_order.html", {"form": form})  # Re-render the page with the form
            else:
                messages.success(request, f"Successfully queried the status of the order.")
                return redirect("order_status", order_id=order_id)
    else:   
        form = QueryOrderForm()
        
    return render(request, "Amazon/query_order.html", {"form": form})

def order_status(request, order_id):
    order = Order.objects.get(id=order_id)
    
    context = {
        'order_id': order.id,
        'status': order.status,
        'dest_x': order.destination_x,
        'dest_y': order.destination_y
    }
    
    return render(request, 'Amazon/order_status.html', context)

def change_destination(request):
    
    if request.method == "POST":
        form = ChangeDestinationForm(request.POST)
        if form.is_valid():
            new_x = form.cleaned_data.get("new_x")
            new_y = form.cleaned_data.get("new_y")
            order_id = form.cleaned_data.get("order_id")
            
            data = {'order_id': order_id,
                    'dest_x': new_x,
                    'dest_y': new_y,
                    }
            response = requests.post('http://server:5000/change-destination', json=data)
            
            
            return redirect("homepage")
    else:   
        form = ChangeDestinationForm()
        
    return render(request, "Amazon/change_destination.html", {"form": form})
