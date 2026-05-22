from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Store Admin / Vendor'),
        ('customer', 'Regular Customer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    store_name = models.CharField(max_length=100, blank=True, null=True, help_text="For Admins: Store brand name")
    gcash_number = models.CharField(max_length=15, blank=True, null=True, help_text="For payment collection tracking")
    account_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Product(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'}, related_name='inventory_items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    # NEW FIELDS FOR IMAGE SUPPORT
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text="Paste an external image link")
    # FIXED: Changed upload_file_to to upload_to
    image_file = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Upload a local jpeg/png image file")

    def __str__(self):
        return f"{self.name} - Shop: {self.seller.store_name or self.seller.user.username}"

class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in {self.customer.username}'s cart"

class Sale(models.Model):
    STATUS_CHOICES = [
        ('unpaid', '🔴 Unpaid / Charged to Credit'),
        ('paid', '🟢 Settled / Paid Off'),
    ]
    DELIVERY_CHOICES = [
        ('pending', '📦 To Be Delivered'),
        ('delivered', '✅ Delivered'),
    ]
    PAYMENT_CONFIRMATION_CHOICES = [
        ('not_sent', '⏳ Payment Not Yet Sent'),
        ('sent', '📱 Payment Sent'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'}, related_name='store_sales')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_recorded = models.DateTimeField(auto_now_add=True)
    
    # Advanced Order Controls
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
    delivery_status = models.CharField(max_length=15, choices=DELIVERY_CHOICES, default='pending')
    customer_payment_status = models.CharField(max_length=15, choices=PAYMENT_CONFIRMATION_CHOICES, default='not_sent')

    def __str__(self):
        return f"Order {self.id} | {self.product.name if self.product else 'Unknown'}"