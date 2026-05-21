# Backend Setup Guide - Django

This guide will help you set up and run the SariSari Store backend locally on your machine.

## 📋 Prerequisites

Before getting started, ensure you have the following installed on your system:

- **Python 3.9+** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager - comes with Python)
- **Git** ([Download](https://git-scm.com/))
- **Virtual Environment** (recommended)

### Verify Installation

```bash
# Check Python version
python --version

# Check pip version
pip --version
```

## 🔧 Installation Steps

### 1. Clone the Repository

```bash
# Navigate to your desired directory
cd path/to/your/projects

# Clone the repository
git clone https://github.com/yourusername/SariSariStoreBackend.git

# Enter the project directory
cd SariSariStoreBackend
```

### 2. Create a Virtual Environment

Creating a virtual environment isolates project dependencies from your system Python.

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

### 3. Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all required packages from requirements.txt
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, create it:
```bash
pip freeze > requirements.txt
```

### 4. Database Setup

```bash
# Apply migrations to set up database
python manage.py migrate

# Create a superuser account (admin)
python manage.py createsuperuser
# Follow the prompts to create username, email, and password
```

### 5. Run the Development Server

```bash
# Start the Django development server
python manage.py runserver
```

The backend will be available at: **http://localhost:8000**

## 🌐 Accessing the Application

### Frontend (Main App)
- **URL**: http://localhost:8000
- Navigate to login or register

### Django Admin Panel
- **URL**: http://localhost:8000/admin
- Login with the superuser credentials you created

### API Endpoints
All API endpoints are available at `http://localhost:8000/`

## 📦 Project Dependencies

### Core Dependencies
- **Django 5.2.1** - Web framework
- **Pillow** - Image processing (for product images)

### Optional Dependencies (for production)
- **gunicorn** - WSGI server
- **psycopg2** - PostgreSQL adapter
- **python-decouple** - Environment variables
- **django-cors-headers** - CORS support

See [DEPENDENCIES.md](DEPENDENCIES.md) for complete list.

## 🗂️ Important Files & Folders

| File/Folder | Purpose |
|-------------|---------|
| `manage.py` | Django management tool |
| `store_project/settings.py` | Main Django configuration |
| `api/models.py` | Database models |
| `api/views.py` | View/Controller logic |
| `api/urls.py` | URL routing |
| `db.sqlite3` | SQLite database (local) |
| `media/` | User-uploaded files (product images) |

## 🔐 Environment Configuration

### Settings Overview

Location: `store_project/settings.py`

Key settings:
```python
DEBUG = True                 # Set to False in production
ALLOWED_HOSTS = []          # Add your domain in production
SECRET_KEY = '...'          # Change this in production
DATABASES = {...}           # SQLite by default
INSTALLED_APPS = [...]      # Active Django apps
```

### For Production

⚠️ **Before deploying to production:**

1. **Change SECRET_KEY**: Generate a new secure key
2. **Set DEBUG = False**: Disable debug mode
3. **Configure ALLOWED_HOSTS**: Add your domain
4. **Use environment variables**: Store sensitive data in `.env`
5. **Use PostgreSQL/MySQL**: Don't use SQLite in production
6. **Set up HTTPS**: Ensure SSL/TLS configuration

## 📝 Common Commands

```bash
# Start development server
python manage.py runserver

# Start on specific port
python manage.py runserver 8080

# Create new Django app
python manage.py startapp appname

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell (for testing)
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic --noinput

# Run tests
python manage.py test

# Check project status
python manage.py check
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution**: Make sure your virtual environment is activated and dependencies are installed.
```bash
# Verify venv is activated (should see (venv) in prompt)
# If not, activate it:
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Issue: Database locked or migration errors

**Solution**: Delete `db.sqlite3` and reapply migrations.
```bash
# Remove old database
rm db.sqlite3

# Reapply migrations
python manage.py migrate
```

### Issue: Static files not loading

**Solution**: Collect static files.
```bash
python manage.py collectstatic --noinput
```

### Issue: Port 8000 already in use

**Solution**: Use a different port.
```bash
python manage.py runserver 8080
```

## 📚 Additional Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/) (if using API)
- [Django Security Documentation](https://docs.djangoproject.com/en/5.2/topics/security/)

## ✅ Verification Checklist

After setup, verify everything is working:

- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip list` shows Django and other packages)
- [ ] Database migrated (`python manage.py migrate` completes without errors)
- [ ] Superuser created (`python manage.py createsuperuser` works)
- [ ] Development server runs (`python manage.py runserver`)
- [ ] Can access http://localhost:8000
- [ ] Can access http://localhost:8000/admin with superuser credentials

---

**Need help?** Check the [README.md](README.md) for more information or raise an issue on GitHub.
