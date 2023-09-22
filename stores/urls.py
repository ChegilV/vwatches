from django.urls import path, reverse
from core.views import index
from . import views

urlpatterns = [
    path("", index, name="home"),
    path('cart/',views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),

    path("collection/", views.collection_items, name="collections"),
    path('collection/all/', views.all_collection, name='all_collection'),
    path('collection/all/<str:name>', views.item_product, name='item_product'),

    path("collection/Armani/", views.armani, name='armani_product'),
    path("collection/Armani/<str:name>", views.item_product, name='item_product'),
    path("collection/Astronic/", views.astronic, name='astronic_product'),
    path("collection/Astronic/<str:name>", views.item_product, name='item_product'),
    path("collection/Ballast/", views.ballast, name='ballast_product'),
    path("collection/Ballast/<str:name>", views.item_product, name='item_product'),
    path("collection/Bulova/", views.bulova, name='bulova_product'),
    path("collection/Bulova/<str:name>", views.item_product, name='item_product'),
    path("collection/California/", views.california, name='california_product'),
    path("collection/California/<str:name>", views.item_product, name='item_product'),
    path("collection/Casio/", views.casio, name='casio_product'),
    path("collection/Casio/<str:name>", views.item_product, name='item_product'),
    path("collection/Citizen/", views.citizen, name='citizen_product'),
    path("collection/Citizen/<str:name>", views.item_product, name='item_product'),
    path("collection/G-Shock/", views.g_shock, name='g_shock_product'),
    path("collection/G-Shock/<str:name>", views.item_product, name='item_product'),
    path("collection/Jason-Hyde/", views.jason_hyde, name='jason_hyde_product'),
    path("collection/Jason-Hyde/<str:name>", views.item_product, name='item_product'),
    path("collection/M2Z/", views.m2z, name='m2z_product'),
    path("collection/M2Z/<str:name>", views.item_product, name='item_product'),
    path("collection/Breitling/", views.breitling, name='breitling_product'),
    path("collection/Breitling/<str:name>", views.item_product, name='item_product'),
    path("collection/Timex/", views.timex, name='timex_product'),
    path("collection/Timex/<str:name>", views.item_product, name='item_product'),
    path("collection/Zodiac/", views.zodiac, name='zodiac_product'),
    path("collection/Zodiac/<str:name>", views.item_product, name='item_product'),

    path('collection/all_sale_products/', views.all_sale_products, name='all_sale_products'),
    path('collection/all_sale_products/<str:name>', views.item_product, name='item_product'),
    path("collection/Sale-M/Armani/", views.sale_armani, name='sale_armani'),
    path("collection/Sale-M/Armani/<str:name>", views.item_product, name='item_product'),
    path("collection/Sale-M/California/", views.sale_california, name='sale_california'),
    path("collection/Sale-M/California/<str:name>", views.item_product, name='item_product'),
    path("collection/Sale-M/G-Shock/", views.sale_g_shock, name='sale_g_shock'),
    path("collection/Sale-M/G-Shock/<str:name>", views.item_product, name='item_product'),

    path("collection/Man-ShopByColor/Black/", views.man_black_color, name='black_man_color'),
    path("collection/Man-ShopByColor/Black/<str:name>", views.item_product, name='item_product'),
    path("collection/Man-ShopByColor/Gold/", views.gold_man_color, name='gold_man_color'),
    path("collection/Man-ShopByColor/Gold/<str:name>", views.item_product, name='item_product'),
    path("collection/Man-ShopByColor/Blue/", views.blue_man_color, name='blue_man_color'),
    path("collection/Man-ShopByColor/Blue/<str:name>", views.item_product, name='item_product'),
    path("collection/Man-ShopByColor/Silver/", views.silver_man_color, name='silver_man_color'),
    path("collection/Man-ShopByColor/Silver/<str:name>", views.item_product, name='item_product'),


    path("collection/Women-ShopByColor/Black/", views.black_women_color, name='black_women_color'),
    path("collection/Women-ShopByColor/Black/<str:name>", views.item_product, name='item_product'),
    path("collection/Women-ShopByColor/Silver/", views.silver_women_color, name='silver_women_color'),
    path("collection/Women-ShopByColor/Silver/<str:name>", views.item_product, name='item_product'),
    path("collection/Women-ShopByColor/Blue/", views.blue_women_color, name='blue_women_color'),
    path("collection/Women-ShopByColor/Blue/<str:name>", views.item_product, name='item_product'),
    path("collection/Women-ShopByColor/Gold/", views.gold_women_color, name='gold_women_color'),
    path("collection/Women-ShopByColor/Gold/<str:name>", views.item_product, name='item_product'),
    path("collection/Women-ShopByColor/Colorful/", views.colorful_women_color, name='colorful_women_color'),
    path("collection/Women-ShopByColor/Colorful/<str:name>", views.item_product, name='item_product'),

    path("collection/Sale-W/G-Shock/", views.sale_w_g_shock, name='sale_w_g_shock'),
    path("collection/Sale-W/G-Shock/<str:name>", views.item_product, name='item_product'),
    path("collection/Sale-W/Jason-Hyde/", views.sale_w_jason_hyde, name='sale_w_jason_hyde'),
    path("collection/Sale-W/Jason-Hyde/<str:name>", views.item_product, name='item_product'),
    path("collection/Sale-W/Timex/", views.sale_w_timex, name='sale_w_timex'),
    path("collection/Sale-W/Timex/<str:name>", views.item_product, name='item_product'),


    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),




]

