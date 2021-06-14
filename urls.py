from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.dish, name='dish'),
    path('accounts/profile/<str:menuType>/<str:menu>/', views.menucard, name='menucard'),
    path('accounts/cart/', views.cart, name='cart'),
    path('accounts/order/', views.order, name='order'),
    path('accounts/order/place', views.place_order, name='place_order'),
    path('accounts/cart/remove/', views.cartRemove, name='cartRemove'),
    path('accounts/cart/add/', views.cartAdd, name='cartAdd'),
    path('accounts/profile/cartData/', views.cartData, name='cartData'),
]
