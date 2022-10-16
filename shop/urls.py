from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('cart', views.cart, name='cart'),
    path('shop-policy', views.shop_policy, name='shop_policy'),
    path('about-tea', views.about_tea, name='about_tea'),
    path('payment-submission', views.payment_submission, name='payment_submission'),

    # Endpoints
    path('add-product-to-cart/<product_id>/', views.add_product_to_cart, name='add_product_to_cart'),
    path('remove-product-from-cart/<product_id>/', views.remove_product_from_cart, name='remove_product_from_cart'),
    path('product-to-cart-detail/<product_to_cart_id>/', views.product_to_cart_detail, name='product_to_cart_detail'),
    path('cart-detail', views.cart_detail, name='cart_detail'),
    path('order-information', views.OrderShippingView.as_view(), name='order_information'),
    path('order-payment', views.OrderPaymentView.as_view(), name='order_payment'),
    path('order-confirmation/<order_id>/', views.order_confirmation, name='order_confirmation'),
]
