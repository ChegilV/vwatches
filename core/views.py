from django.shortcuts import render
from stores.models import Sale_Product, Order, Customer
from django.contrib.auth.decorators import login_required
from stores.views import all_sale_products
from stores.utils import cookieCart, cartData
from registApp.decorators import unauthenticated_user, allowed_users

# Create your views here.

# @login_required(login_url='login')

def index(request):
    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']

    three_sale_products = Sale_Product.objects.all().order_by("id")[:3]
    context = {"three_sale_products": three_sale_products, "cartItems":cartItems}
    return render(request, 'core/html/index.html', context)

def hok(request):
    data = cartData(request)
    cartItems = data['cartItems']
    if request.method == "GET":
        searched = request.GET.get("searched")
        post = Sale_Product.objects.filter(name__icontains=searched)
        return render(request, 'core/html/h.html', {"post":post, 'cartItems':cartItems})


