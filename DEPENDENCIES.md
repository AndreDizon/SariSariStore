# Dependencies Documentation

This document lists all dependencies required for the SariSari Store project, organized by component (Backend/Frontend) and environment (Development/Production).

---

## 🐍 Backend Dependencies

### Django Backend (Python)

The backend uses Python and Django. Ensure you have Python 3.9+ installed.

#### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **Django** | 5.2.1 | Web framework |
| **Pillow** | Latest | Image processing (product images) |

#### Optional Dependencies (for enhanced features)

| Package | Purpose | Notes |
|---------|---------|-------|
| **djangorestframework** | REST API development | If building REST API |
| **django-cors-headers** | CORS support | For frontend-backend communication |
| **django-filter** | Advanced filtering | For product filtering |
| **celery** | Async task queue | For background jobs |
| **redis** | Cache/message broker | Works with Celery |
| **gunicorn** | WSGI server | For production deployment |
| **psycopg2-binary** | PostgreSQL adapter | If using PostgreSQL |
| **python-decouple** | Environment variables | For configuration management |
| **python-dotenv** | .env file support | For local environment setup |

#### Production-Only Dependencies

| Package | Purpose |
|---------|---------|
| **whitenoise** | Serve static files efficiently |
| **sentry-sdk** | Error tracking |
| **django-debug-toolbar** | Debugging (development only, disable in prod) |

### Creating requirements.txt

**Step 1**: Ensure all packages are installed in your virtual environment.

**Step 2**: Generate requirements.txt:

```bash
# Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Generate requirements file
pip freeze > requirements.txt
```

**Step 3**: Example `requirements.txt` for this project:

```
Django==5.2.1
Pillow>=10.0.0
djangorestframework==3.14.0
django-cors-headers==4.3.0
gunicorn==21.2.0
python-dotenv==1.0.0
psycopg2-binary==2.9.9
```

### Installing Dependencies

```bash
# Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install from requirements.txt
pip install -r requirements.txt

# Or install individual packages
pip install Django==5.2.1
pip install Pillow
pip install djangorestframework
```

### Verifying Installation

```bash
# List installed packages
pip list

# Check specific package
pip show Django

# Check for outdated packages
pip list --outdated
```

---

## 🎨 Frontend Dependencies

### Option 1: Django Templates (Current)

**No additional dependencies required** - Uses built-in Django templating engine.

**Client-Side (Optional):**
- Bootstrap (CSS framework)
- jQuery (if needed for interaction)
- Vanilla JavaScript

### Option 2: React Frontend

#### System Requirements
- **Node.js**: 16+ LTS or 18+
- **npm**: 7+ (comes with Node.js)
- **yarn**: 3+ (optional, alternative to npm)

#### Core Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| **react** | UI library | Latest |
| **react-dom** | React rendering | Latest |
| **react-router-dom** | Routing/Navigation | Latest |
| **axios** | HTTP client | Latest |

#### Development Dependencies

| Package | Purpose |
|---------|---------|
| **@vitejs/plugin-react** | Vite React plugin |
| **eslint** | Code linting |
| **prettier** | Code formatting |

#### Recommended UI Libraries

```bash
# Tailwind CSS (recommended for SariSari Store)
npm install -D tailwindcss postcss autoprefixer

# OR Bootstrap
npm install bootstrap react-bootstrap

# OR Material-UI
npm install @mui/material @emotion/react @emotion/styled
```

#### Creating package.json

```bash
# Navigate to frontend directory
cd sari-sari-store-frontend

# Initialize npm project
npm init -y

# Install dependencies
npm install react react-dom react-router-dom axios
npm install -D @vitejs/plugin-react vite
```

**Example package.json:**

```json
{
  "name": "sari-sari-store-frontend",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0"
  }
}
```

### Option 3: Vue.js Frontend

#### Core Dependencies

```bash
npm install vue vue-router axios
```

#### Example package.json for Vue

```json
{
  "name": "sari-sari-store-frontend",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.3.0",
    "vue-router": "^4.2.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^4.5.0",
    "vite": "^5.0.0"
  }
}
```

---

## 🗂️ System Dependencies (One-Time Setup)

### Required Software

| Software | Minimum Version | Purpose |
|----------|-----------------|---------|
| **Python** | 3.9 | Backend runtime |
| **pip** | 20.0 | Python package manager |
| **Node.js** | 16 LTS | Frontend runtime |
| **npm** | 7 | JavaScript package manager |
| **Git** | 2.25 | Version control |

### Installation Links

- **Python**: https://www.python.org/downloads/
- **Node.js**: https://nodejs.org/ (includes npm)
- **Git**: https://git-scm.com/

### Verify Installation

```bash
# Check Python
python --version

# Check pip
pip --version

# Check Node.js
node --version

# Check npm
npm --version

# Check Git
git --version
```

---

## 📊 Dependency Tree

### Backend Architecture

```
Django Project
├── Django Framework
│   ├── Authentication
│   ├── ORM (Database)
│   ├── Templating
│   └── Admin Interface
├── Pillow (Image Processing)
└── Optional:
    ├── djangorestframework
    ├── django-cors-headers
    ├── celery + redis
    └── gunicorn (production)
```

### Frontend (React) Architecture

```
React Application
├── React Core
│   ├── react
│   └── react-dom
├── Routing
│   └── react-router-dom
├── HTTP Client
│   └── axios
└── UI Framework
    ├── Tailwind CSS OR
    ├── Bootstrap OR
    └── Material-UI
```

---

## 🔄 Updating Dependencies

### Check for Outdated Packages

**Backend:**
```bash
pip list --outdated
```

**Frontend:**
```bash
npm outdated
```

### Update Packages

**Backend:**
```bash
# Update specific package
pip install --upgrade Django

# Update all packages in requirements.txt
pip install --upgrade -r requirements.txt
```

**Frontend:**
```bash
# Update specific package
npm update react

# Update all packages
npm update
```

### Security Audits

**Backend:**
```bash
pip audit  # Check for known vulnerabilities
```

**Frontend:**
```bash
npm audit  # Check for vulnerabilities
npm audit fix  # Auto-fix vulnerabilities
```

---

## 🚀 Production Dependencies

### Recommended Production Setup

**Backend:**
```
Django==5.2.1
Pillow>=10.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
django-cors-headers==4.3.0
python-dotenv==1.0.0
whitenoise==6.6.0
```

**Frontend:**
Built assets only - no runtime dependencies needed

### Environment-Specific Installation

Create multiple requirements files:

```bash
# requirements-dev.txt (Development)
-r requirements.txt
django-debug-toolbar==4.2.0
coverage==7.3.0

# requirements-prod.txt (Production)
-r requirements.txt
gunicorn==21.2.0
whitenoise==6.6.0
sentry-sdk==1.38.0
```

Install based on environment:
```bash
# Development
pip install -r requirements-dev.txt

# Production
pip install -r requirements-prod.txt
```

---

## 🔐 Security Considerations

### Vulnerable Packages

Regular checks for security vulnerabilities:

```bash
# Backend
pip audit

# Frontend
npm audit
```

### Pinning Versions

To ensure consistency across environments, use specific versions in requirements.txt:

```
# Good - pinned version
Django==5.2.1
Pillow==10.0.0

# Not recommended - loose version
Django>=5.0
Pillow
```

---

## 📝 Dependency Installation Checklist

- [ ] Python 3.9+ installed
- [ ] pip updated to latest version
- [ ] Virtual environment created
- [ ] requirements.txt present
- [ ] All dependencies installed without errors
- [ ] Django migrations applied
- [ ] Superuser created
- [ ] Development server runs without errors
- [ ] Node.js 16+ installed (if using React/Vue)
- [ ] npm dependencies installed (`npm install`)
- [ ] Frontend dev server runs without errors

---

## 🆘 Troubleshooting

### Issue: "No module named 'django'"

```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install Django
pip install Django==5.2.1
```

### Issue: Pillow fails to install

```bash
# On Windows, may need to install from wheel
pip install Pillow --only-binary :all:

# On macOS/Linux
brew install libjpeg  # macOS
sudo apt-get install libjpeg-dev  # Ubuntu/Debian
pip install Pillow
```

### Issue: npm install fails

```bash
# Clear npm cache
npm cache clean --force

# Try installing again
npm install

# Or use npm ci for production
npm ci
```

---

## 📚 Resources

- [Python Package Index (PyPI)](https://pypi.org/)
- [npm Registry](https://www.npmjs.com/)
- [Django Packages](https://djangopackages.org/)
- [React Ecosystem](https://react.dev/)

---

**Last Updated**: May 2026
