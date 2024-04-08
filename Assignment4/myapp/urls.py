from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('products/', views.ProductsList.as_view(), name='products-list'),
    path('products/<int:pk>/', views.ProductsDetail.as_view(), name='products-detail'),
]
