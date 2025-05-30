from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Itens
    path('item/new/', views.item_create, name='item_create'),
    path('item/edit/<int:pk>/', views.item_update, name='item_update'),
    path('item/delete/<int:pk>/', views.item_delete, name='item_delete'),
    # Categorias
    path('category/new/', views.category_create, name='category_create'),
    path('category/edit/<int:pk>/', views.category_update, name='category_update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
]