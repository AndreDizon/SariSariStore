from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('setup-profile/', views.setup_profile, name='setup_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    
    # Logistics Action Triggers
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), # <-- NEW
    path('cart/checkout/', views.checkout_cart, name='checkout_cart'),
    path('sales/payment-toggle/<int:sale_id>/', views.toggle_customer_payment, name='toggle_customer_payment'),
    path('sales/admin-pay/<int:sale_id>/', views.toggle_admin_payment, name='toggle_admin_payment'),
    path('sales/admin-delivery/<int:sale_id>/', views.toggle_admin_delivery, name='toggle_admin_delivery'),
    path('products/add/', views.add_product, name='add_product'),
]