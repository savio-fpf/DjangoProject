from django.urls import path
from . import views

urlpatterns = [
    # Items
    path('item/', views.item_list, name='item_list'),

    path('item/new/', views.item_create, name='item_create'),

    path('item/edit/<int:pk>/', views.item_update, name='item_update'),
    path('item/delete/<int:pk>/', views.item_delete, name='item_delete'),

    path('autor/edit/<int:pk>/', views.author_update, name='author_update'),
    path('autor/delete/<int:pk>/', views.author_delete, name='author_delete'),

    path('category/edit/<int:pk>/', views.category_update, name='category_update'),
    path('category/delete/<int:pk>/', views.category_delete, name='category_delete'),
]
