from django.contrib import admin
from .models import UserProfile, Product, Sale

# Register the new role-based models into the built-in Django Admin portal
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Sale)