# Frontend Setup Guide

This guide will help you set up and run the SariSari Store frontend. The frontend is designed to communicate with the Django backend API.

## 📋 Frontend Technology Recommendations

The current project uses **Django Templates** for the frontend. For a modern, scalable approach, consider one of these options:

### Option 1: React (Recommended for Single Page Application)
- **Best for**: Modern, interactive UI with real-time updates
- **Setup time**: ~30 minutes
- **Difficulty**: Medium

### Option 2: Vue.js
- **Best for**: Progressive enhancement, lighter bundle size
- **Setup time**: ~30 minutes
- **Difficulty**: Medium

### Option 3: Continue with Django Templates
- **Best for**: Server-rendered pages, rapid development
- **Setup time**: Minimal
- **Difficulty**: Easy

---

## 🎯 Current Django Template Setup

The current frontend uses Django templates and HTML. Here's how to work with it:

### Project Structure

```
api/templates/
├── dashboard.html           # Main landing/dashboard
├── auth/
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── setup_profile.html  # User profile setup
└── dashboards/
    ├── admin_dashboard.html   # Admin/Vendor dashboard
    └── customer_dashboard.html # Customer dashboard
```

### Running the Frontend (Django Templates)

The frontend is served by the Django backend. To run it:

```bash
# Make sure you're in the project directory
cd SariSariStore

# Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Run Django development server
python manage.py runserver

# Access frontend at:
# http://localhost:8000
```

### Editing Templates

Templates are located in `api/templates/` directory. Edit `.html` files directly:

```bash
# Example: Edit login page
# Open: api/templates/auth/login.html
```

---

## 🚀 Switching to React (Modern Approach)

If you want to build a modern React frontend, follow these steps:

### Prerequisites

- **Node.js 16+** ([Download](https://nodejs.org/))
- **npm** (comes with Node.js) or **yarn**

### 1. Create React App

```bash
# Navigate to your projects folder (outside SariSariStore)
cd path/to/your/projects

# Create React app
npx create-react-app sari-sari-store-frontend

# Navigate into frontend folder
cd sari-sari-store-frontend
```

### 2. Install Required Packages

```bash
# Install axios for API calls
npm install axios

# Install React Router for navigation
npm install react-router-dom

# Install state management (optional but recommended)
npm install zustand
# OR
npm install redux @reduxjs/toolkit react-redux
```

### 3. Configure API Connection

Create `.env` file in frontend root:

```env
REACT_APP_API_URL=http://localhost:8000
```

### 4. Create API Service

Create `src/services/api.js`:

```javascript
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Add CSRF token to requests if needed
api.interceptors.request.use((config) => {
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
  if (csrftoken) {
    config.headers['X-CSRFToken'] = csrftoken;
  }
  return config;
});

export default api;
```

### 5. Create Main Components

**src/App.js:**
```javascript
import React, { useState, useEffect } from 'react';
import api from './services/api';
import './App.css';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch data from backend
    const fetchProducts = async () => {
      try {
        const response = await api.get('/products/');
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div className="App">
      <h1>SariSari Store</h1>
      <div className="products">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <h3>{product.name}</h3>
            <p>Price: ${product.price}</p>
            <p>Stock: {product.stock}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
```

### 6. Run React Development Server

```bash
npm start

# Frontend will be available at: http://localhost:3000
```

### 7. Enable CORS in Django

In `store_project/settings.py`, add:

```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
]
```

Install django-cors-headers:
```bash
pip install django-cors-headers
```

---

## 🎨 Vue.js Alternative

If you prefer Vue.js:

```bash
# Create Vue app
npm create vite@latest sari-sari-store-frontend -- --template vue

cd sari-sari-store-frontend

# Install dependencies
npm install

# Install axios
npm install axios

# Run development server
npm run dev
```

---

## 📦 Frontend Project Structure (React Example)

```
sari-sari-store-frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Login.jsx
│   │   ├── Register.jsx
│   │   ├── ProductList.jsx
│   │   ├── Cart.jsx
│   │   ├── AdminDashboard.jsx
│   │   └── CustomerDashboard.jsx
│   ├── services/
│   │   └── api.js               # Backend API calls
│   ├── App.jsx
│   ├── App.css
│   └── index.js
├── .env
├── package.json
├── package-lock.json
└── README.md
```

## 🔌 API Integration Examples

### Login
```javascript
const login = async (username, password) => {
  try {
    const response = await api.post('/login', {
      username,
      password,
    });
    return response.data;
  } catch (error) {
    console.error('Login failed:', error);
  }
};
```

### Fetch Products
```javascript
const fetchProducts = async () => {
  try {
    const response = await api.get('/products/');
    return response.data;
  } catch (error) {
    console.error('Error fetching products:', error);
  }
};
```

### Add to Cart
```javascript
const addToCart = async (productId, quantity) => {
  try {
    const response = await api.post('/add-to-cart', {
      product_id: productId,
      quantity,
    });
    return response.data;
  } catch (error) {
    console.error('Error adding to cart:', error);
  }
};
```

## 🔄 Running Both Frontend & Backend

To run both simultaneously:

### Terminal 1 - Backend
```bash
cd SariSariStore
source venv/bin/activate  # or venv\Scripts\activate on Windows
python manage.py runserver
# Backend runs at http://localhost:8000
```

### Terminal 2 - Frontend
```bash
cd sari-sari-store-frontend
npm start
# Frontend runs at http://localhost:3000 (React) or http://localhost:5173 (Vue)
```

## 📱 Responsive Design Tips

For a mobile-friendly frontend:

1. **Use CSS Framework**: Bootstrap, Tailwind CSS, Material-UI
2. **Mobile-First Approach**: Design for mobile first, then scale up
3. **Test on Devices**: Use browser DevTools or actual devices

```bash
# Example: Add Tailwind CSS to React
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

## 📝 Common Frontend Tasks

| Task | Command |
|------|---------|
| Start dev server | `npm start` (React) or `npm run dev` (Vue) |
| Build for production | `npm run build` |
| Install package | `npm install package-name` |
| Update dependencies | `npm update` |
| Check for vulnerabilities | `npm audit` |

## 🐛 Troubleshooting

### Issue: CORS errors when calling backend

**Solution**: Enable CORS in Django backend (see section above)

### Issue: API returns 404

**Solution**: Check that backend is running and API endpoint matches

### Issue: Port 3000 already in use

**Solution**: Use different port
```bash
PORT=3001 npm start  # React
npm run dev -- --port 3001  # Vue
```

## 📚 Useful Resources

- [React Documentation](https://react.dev/)
- [Vue.js Documentation](https://vuejs.org/)
- [Axios Documentation](https://axios-http.com/)
- [Django REST API Guide](https://www.django-rest-framework.org/)

---

**Choose your preferred option and follow the appropriate setup guide above!**
