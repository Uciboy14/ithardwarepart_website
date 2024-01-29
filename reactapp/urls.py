from django.urls import path
from .views import (
    UserRegister,
    UserLogin,
    UserLogout,
    UserView,
    CategoryView,
    ProductView,
    CartView,
    CartItemView,
    OrderView,
    ProductDetailView,
)

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('logout', UserLogout.as_view(), name='logout'),
    path('categories/', CategoryView.as_view(), name='category_list'),
    path('products/', ProductView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('carts/', CartView.as_view(), name='cart_list'),
    path('cartitems/', CartItemView.as_view(), name='cartitem_list'),
    path('orders/', OrderView.as_view(), name='order_list'),
]
