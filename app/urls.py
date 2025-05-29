from django.urls import path
from . import views

urlpatterns = [
    #path('', views.item_list, name='item_list'),
    #path('new/', views.item_create, name='item_create'),
    #path('edit/<int:pk>/', views.item_update, name='item_update'),
    #path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('', views.category_list, name='category_list'),
    path('new/', views.category_create, name='category_create'),
    path('edit/<int:pk>/', views.category_update, name='category_update'),
    path('delete/<int:pk>/', views.category_delete, name='category_delete'),

]
