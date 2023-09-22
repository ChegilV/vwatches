from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime
from django.db.models import Q
from .utils import cookieCart, cartData, guestOrder


def all_collection(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems': cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/all.html", context)


def collection_items(request):

    data = cartData(request)
    cartItems = data['cartItems']



    collection_products = CollectionItems.objects.all().order_by("brandName")
    context = {"collection_products":collection_products,'cartItems':cartItems }
    return render(request, "stores/html/collection_items.html", context)


def armani(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/armani_product.html", context)


def astronic(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/astronic_product.html", context)

def ballast(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/ballast_product.html", context)

def bulova(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/bulova_product.html", context)

def california(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/california_product.html", context)


def casio(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/casio_product.html", context)

def citizen(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/citizen_product.html", context)

def g_shock(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/g_shock_product.html", context)

def jason_hyde(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/jason_hyde_product.html", context)


def breitling(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/breitling_product.html", context)


def m2z(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/m2z_product.html", context)

def timex(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/timex_product.html", context)

def zodiac(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/brands/zodiac_product.html", context)

def all_sale_products(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {"sale_products": sale_products,'cartItems':cartItems}
    return render(request, 'stores/html/all_sale_products.html', context)\

def sale_armani(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_on_sale_man/armani_product.html", context)

def sale_california(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_on_sale_man/california_product.html", context)

def sale_g_shock(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_on_sale_man/g_shock_product.html", context)

def man_black_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/black_man_product.html", context)

def gold_man_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/gold_man_product.html", context)


def blue_man_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/blue_man_product.html", context)


def silver_man_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/silver_man_product.html", context)

def black_women_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/black_women_product.html", context)

def silver_women_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/silver_women_product.html", context)


def blue_women_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/blue_women_product.html", context)


def gold_women_color(request):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/gold_women_product.html", context)


def colorful_women_color(request,):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.exclude(Q(color="black") | Q(color="silver") | Q(color="blue") | Q(color="gold"))
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_by_color/colorful_women_product.html", context)


def sale_w_g_shock(request,):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_on_sale_women/g_shock_product.html", context)


def sale_w_jason_hyde(request,):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_on_sale_women/jason_hyde_product.html", context)


def sale_w_timex(request,):
    data = cartData(request)
    cartItems = data['cartItems']

    sale_products = Sale_Product.objects.all()
    context = {'cartItems':cartItems, "sale_products": sale_products}
    return render(request, "stores/html/shop_on_sale_women/timex_product.html", context)

def item_product(request, name, ):
    data = cartData(request)
    cartItems = data['cartItems']


    sale_products = Sale_Product.objects.filter(name=name).first()


    context={"sale_products": sale_products, 'cartItems':cartItems}
    return render(request, "stores/html/product_item.html", context)





# @login_required(login_url='login')
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context = {'items': items, 'order':order, 'cartItems':cartItems, }
    return render(request, "stores/html/cart.html", context)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def checkout(request):


    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order':order, 'cartItems': cartItems}
    return render(request, "stores/html/checkout_watch.html", context)


def updateItem(request):
    data = json.loads(request.body)
    print(data)
    action = data['action']
    productId = data['productId']

    print("aCtion: ", action)
    print("productID: ", productId)


    customer = request.user.customer
    product = Sale_Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == "removeAll":
        orderItem.quantity = (orderItem.quantity - orderItem.quantity)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:

        customer, order = guestOrder(request, data)

    total = float(data["form"]["total"])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            phoneNumber=data["shipping"]['phone_number'],
            address=data["shipping"]['address'],
            postalCode=data["shipping"]['postalcode'],
            city=data["shipping"]['city'],

        )

    return JsonResponse("PaymentComplete!", safe=False)

