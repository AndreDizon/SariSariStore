from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.db.models import Sum, Q
from .models import UserProfile, Product, Sale, CartItem
from django.contrib.auth.models import User

# Standard Logins Redirect rules remain exactly the same
def login_view(request):
    if request.user.is_authenticated: 
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        user = authenticate(username=username, password='password123')
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'auth/login.html', {'error': 'Invalid credentials.'})
    return render(request, 'auth/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'error': 'Username already taken.'})
        user = User.objects.create_user(username=username, email=email, password='password123')
        UserProfile.objects.create(user=user, role=role)
        login(request, user)
        return redirect('setup_profile')
    return render(request, 'auth/register.html')

@login_required
def setup_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.phone_number = request.POST.get('phone_number')
        profile.delivery_address = request.POST.get('delivery_address')
        profile.gcash_number = request.POST.get('gcash_number')
        if profile.role == 'admin':
            profile.store_name = request.POST.get('store_name')
        profile.save()
        return redirect('dashboard')
    return render(request, 'auth/setup_profile.html', {'profile': profile})

@login_required
def dashboard(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user, role='admin')

    # Core Search & Filter Variables Extraction
    search_query = request.GET.get('search', '')
    shop_filter = request.GET.get('shop_filter', '')
    ledger_search = request.GET.get('ledger_search', '')

    if profile.role == 'admin':
        # DATABASE HEALER: Automatically claim unassigned database items for this admin session
        Product.objects.filter(seller__isnull=True).update(seller=profile)

        # Admin displays orders intended for their specific shop profile
        sales_records = Sale.objects.filter(seller=profile).order_by('-date_recorded')
        products = Product.objects.filter(seller=profile)
        
        # Filter products managed under current admin shop view if query exists
        if search_query:
            products = products.filter(name__icontains=search_query)

        customers = UserProfile.objects.filter(role='customer')
        if ledger_search:
            customers = customers.filter(Q(user__username__icontains=ledger_search) | Q(phone_number__icontains=ledger_search))

        customer_ledgers = []
        for c in customers:
            # Aggregate debts incurred only within THIS merchant shop environment context
            unpaid_debt = Sale.objects.filter(customer=c.user, seller=profile, status='unpaid').aggregate(total=Sum('total_amount'))['total'] or 0
            customer_ledgers.append({
                'username': c.user.username,
                'phone_number': c.phone_number,
                'outstanding_debt': unpaid_debt
            })
            
        context = {
            'products': products,
            'sales_records': sales_records,
            'customer_ledgers': customer_ledgers,
            'profile': profile,
            'search_query': search_query,
            'ledger_search': ledger_search
        }
        return render(request, 'dashboards/admin_dashboard.html', context)
        
    else: # Customer Global Multi-Vendor Catalogue View Interface
        all_products = Product.objects.filter(stock__gt=0)
        shops = UserProfile.objects.filter(role='admin').exclude(store_name__isnull=True).exclude(store_name='')

        if search_query:
            all_products = all_products.filter(name__icontains=search_query)
        if shop_filter:
            all_products = all_products.filter(seller_id=shop_filter)

        cart_items = CartItem.objects.filter(customer=request.user)
        cart_total = sum(item.product.price * item.quantity for item in cart_items)
        personal_sales = Sale.objects.filter(customer=request.user).order_by('-date_recorded')
        unpaid_debt = personal_sales.filter(status='unpaid').aggregate(total=Sum('total_amount'))['total'] or 0

        context = {
            'products': all_products,
            'shops': shops,
            'cart_items': cart_items,
            'cart_total': cart_total,
            'personal_sales': personal_sales,
            'outstanding_debt': unpaid_debt,
            'profile': profile,
            'search_query': search_query,
            'shop_filter': shop_filter
        }
        return render(request, 'dashboards/customer_dashboard.html', context)

# 🛒 NEW FEATURE ENGINE ACTIONS: CART MANAGEMENT & VERIFICATIONS
@login_required
def add_to_cart(request, product_id):
    if request.user.profile.role == 'customer':
        product = get_object_or_404(Product, id=product_id)
        qty = int(request.POST.get('quantity', 1))
        
        if product.stock >= qty:
            cart_item, created = CartItem.objects.get_or_create(customer=request.user, product=product)
            if not created:
                cart_item.quantity += qty
            else:
                cart_item.quantity = qty
            cart_item.save()
    return redirect('dashboard')

@login_required
def checkout_cart(request):
    if request.user.profile.role == 'customer':
        cart_items = CartItem.objects.filter(customer=request.user)
        for item in cart_items:
            product = item.product
            if product.stock >= item.quantity:
                # Deduct master records allocation levels
                product.stock -= item.quantity
                product.save()
                
                # Split transactions into distinct multi-vendor tracking entries automatically
                Sale.objects.create(
                    customer=request.user,
                    seller=product.seller,
                    product=product,
                    quantity=item.quantity,
                    total_amount=product.price * item.quantity,
                    status='unpaid',
                    delivery_status='pending',
                    customer_payment_status='not_sent'
                )
        cart_items.delete() # Wipe active database cart contents clear on checkout confirmation
    return redirect('dashboard')

@login_required
def toggle_customer_payment(request, sale_id):
    if request.user.profile.role == 'customer':
        sale = get_object_or_404(Sale, id=sale_id, customer=request.user)
        sale.customer_payment_status = 'sent' if sale.customer_payment_status == 'not_sent' else 'not_sent'
        sale.save()
    return redirect('dashboard')

@login_required
def toggle_admin_payment(request, sale_id):
    if request.user.profile.role == 'admin':
        sale = get_object_or_404(Sale, id=sale_id, seller=request.user.profile)
        sale.status = 'paid' if sale.status == 'unpaid' else 'unpaid'
        sale.save()
    return redirect('dashboard')

@login_required
def toggle_admin_delivery(request, sale_id):
    if request.user.profile.role == 'admin':
        sale = get_object_or_404(Sale, id=sale_id, seller=request.user.profile)
        sale.delivery_status = 'delivered' if sale.delivery_status == 'pending' else 'pending'
        sale.save()
    return redirect('dashboard')

@login_required
def add_product(request):
    if request.method == 'POST' and request.user.profile.role == 'admin':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image_url = request.POST.get('image_url')
        image_file = request.FILES.get('image_file') # Captures direct file uploads

        Product.objects.create(
            seller=request.user.profile,
            name=name,
            price=price,
            stock=stock,
            image_url=image_url if image_url else None,
            image_file=image_file if image_file else None
        )
    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def remove_from_cart(request, item_id):
    if request.user.profile.role == 'customer':
        cart_item = get_object_or_404(CartItem, id=item_id, customer=request.user)
        cart_item.delete()
    return redirect('dashboard')

@login_required
def delete_product(request, product_id):
    # Security check: ensures the product exists AND belongs to the logged-in admin vendor
    product = get_object_or_404(Product, id=product_id, seller=request.user.profile)
    
    if request.method == "POST":
        product.delete()
        
    return redirect('dashboard')