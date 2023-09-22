from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.email)

class CollectionItems(models.Model):
    brandName = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url



class Sale_Product(models.Model):
    brand_name= models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    sex = models.CharField(max_length=20, null=True)
    image = models.ImageField(null=True, blank=True)
    color = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Images(models.Model):
    product = models.ForeignKey(Sale_Product, on_delete=models.CASCADE, blank=True, null=True)
    imagesList = models.ImageField(upload_to='pics', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)




class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping=True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total




class OrderItem(models.Model):
    product = models.ForeignKey(Sale_Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True,)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        if self.product.sale_price is not None:
            total = self.product.sale_price * self.quantity
        else:
            total = self.product.price * self.quantity
        return total





class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    phoneNumber = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=200, null=True)
    postalCode = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=30, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str(self):
        return self.address