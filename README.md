# SariSari Store - E-Commerce Platform

A web-based e-commerce platform built with **Django** (backend) for managing a sari-sari store with admin vendors and customers. The platform supports product inventory management, shopping cart, sales tracking, and user authentication with role-based access.

## 🎯 Project Overview

**SariSari Store** is a digital marketplace designed to help traditional sari-sari store owners manage their inventory and customers. The system supports:

- **Admin/Vendor Dashboard**: Manage products, prices, inventory, and sales
- **Customer Portal**: Browse products, add to cart, track orders, and manage deliveries
- **Payment & Delivery Tracking**: Track payment status and delivery status
- **User Roles**: Admin/Vendor and Customer roles with different permissions

## 📋 Tech Stack

### Backend
- **Framework**: Django 5.2.1
- **Database**: SQLite (development), upgradeable to PostgreSQL
- **Authentication**: Django built-in authentication + custom UserProfile model
- **Image Handling**: Django ImageField with local and URL-based storage
- **Static Files**: Django staticfiles

### Frontend
- To be implemented (React/Vue recommended)

## 📁 Project Structure

```
SariSariStoreBackend/
├── api/                          # Main application
│   ├── models.py                 # Database models (UserProfile, Product, Sale, CartItem)
│   ├── views.py                  # View logic (authentication, dashboards, cart)
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Django admin configuration
│   ├── templates/
│   │   ├── dashboard.html        # Main dashboard
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── setup_profile.html
│   │   └── dashboards/
│   │       ├── admin_dashboard.html
│   │       └── customer_dashboard.html
│   └── migrations/               # Database migrations
├── store_project/                # Project settings
│   ├── settings.py               # Django configuration
│   ├── urls.py                   # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── media/                        # User-uploaded files (product images)
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django management tool
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Quick Start

### Backend Setup
See [SETUP_BACKEND.md](SETUP_BACKEND.md) for detailed backend setup instructions.

### Frontend Setup
See [SETUP_FRONTEND.md](SETUP_FRONTEND.md) for detailed frontend setup instructions.

### Dependencies
See [DEPENDENCIES.md](DEPENDENCIES.md) for a complete list of dependencies.

## 📚 Key Features

### User Management
- User registration with role selection (Admin/Customer)
- Profile setup (phone, delivery address, GCash number)
- Role-based access control (RBAC)

### Product Management (Admin)
- Add/edit/delete products
- Upload product images (local files or URLs)
- Track inventory and stock levels
- View sales reports

### Shopping (Customer)
- Browse products from various sellers
- Add products to cart
- View cart and adjust quantities
- Place orders

### Sales & Delivery Tracking
- Track order status (Unpaid/Paid)
- Track delivery status (Pending/Delivered)
- Payment method tracking (Cash/GCash)

## 🔐 Security Notes

⚠️ **Important**: The current setup has hardcoded passwords and debug mode enabled for development. Before production deployment:

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False` in `settings.py`
3. Set `ALLOWED_HOSTS` with your domain
4. Implement proper password authentication
5. Use environment variables for sensitive data

## 📖 API Endpoints

### Authentication
- `POST /login` - User login
- `POST /register` - User registration
- `GET /logout` - User logout

### User Profile
- `GET /setup-profile` - Setup user profile
- `POST /setup-profile` - Save profile changes

### Dashboard
- `GET /dashboard` - Main dashboard (role-based redirect)
- `GET /admin-dashboard` - Admin/vendor dashboard
- `GET /customer-dashboard` - Customer dashboard

### Products (Admin)
- `POST /add-product` - Add new product
- `POST /edit-product/<id>` - Edit product
- `GET /delete-product/<id>` - Delete product

### Shopping Cart
- `POST /add-to-cart` - Add product to cart
- `GET /cart` - View cart
- `POST /remove-from-cart` - Remove from cart

### Sales
- `GET /sales` - View sales history
- `POST /checkout` - Create order from cart

## 🛠️ Development Commands

```bash
# Run development server
python manage.py runserver

# Create database tables
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Access Django admin panel
# Navigate to http://localhost:8000/admin

# Collect static files
python manage.py collectstatic
```

## 📞 Support & Contact

For issues, questions, or contributions, please create an issue or contact the development team.

---

**Last Updated**: May 2026
