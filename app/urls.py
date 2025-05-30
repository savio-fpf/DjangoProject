from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('new/items/', views.item_create, name='item_create'),
    path('edit/items<int:pk>/', views.item_update, name='item_update'),
    path('items/delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('new/publishers/', views.publisher_create, name='publisher_create'),
    path('edit/publishers/<int:pk>/', views.publisher_update, name='publisher_update'),
    path('delete/publishers/<int:pk>/', views.publisher_delete, name='publisher_delete'),
]