from django.urls import path, include

from . import views
from stores import views as viewsStor


app_name = 'core'

urlpatterns = [
    path('', views.index, name='my_home'),
    path('collection/', viewsStor.collection_items, name='collections' ),
    path('hok/', views.hok, name='hok'),



]