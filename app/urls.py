from django.urls import path
from . import views

urlpatterns = [
    ##item
    path('', views.item_list, name='item_list'),
    path('/item/new', views.item_create, name='item_create'),
    path('/item/edit/<int:pk>/', views.item_update, name='item_update'),
    path('/item/delete/<int:pk>/', views.item_delete, name='item_delete'),
    ##categoria
    path('/categoria', views.categoria_list(), name='categoria_list'),
    path('/categoria/new/', views.item_create, name='item_create'),
    path('/categoria/edit/<int:pk>/', views.item_update, name='item_update'),
    path('/categoria/delete/<int:pk>/', views.item_delete, name='item_delete'),
]
