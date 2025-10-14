# EventHub Deployment Guide

## Deployment Overview

EventHub is deployed using:
- **Backend**: Render (Flask API)
- **Frontend**: Netlify (React SPA)
- **Database**: PostgreSQL on Render

## Backend Deployment (Render)

### 1. Prepare for Deployment
```bash
# Ensure requirements.txt is up to date
pip freeze > requirements.txt

# Create Procfile for Render
echo "web: gunicorn app:app" > Procfile
```

### 2. Environment Variables
Set these in Render dashboard:
```
DATABASE_URL=postgresql://...
JWT_SECRET_KEY=your-production-secret
MPESA_CONSUMER_KEY=your-mpesa-key
MPESA_CONSUMER_SECRET=your-mpesa-secret
MPESA_SHORTCODE=your-shortcode
MPESA_PASSKEY=your-passkey
SENDGRID_API_KEY=your-sendgrid-key
CLOUDINARY_URL=your-cloudinary-url
FLASK_ENV=production
```

### 3. Deploy Steps
1. Connect GitHub repository to Render
2. Select Python environment
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`
5. Add environment variables
6. Deploy

## Frontend Deployment (Netlify)

### 1. Build Configuration
Create `netlify.toml`:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  VITE_API_URL = "https://your-backend-url.onrender.com/api"
```

### 2. Environment Variables
Set in Netlify dashboard:
```
VITE_API_URL=https://your-backend-url.onrender.com/api
VITE_MPESA_SHORTCODE=174379
```

### 3. Deploy Steps
1. Connect GitHub repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Add environment variables
5. Deploy

## Database Setup

### 1. PostgreSQL on Render
1. Create PostgreSQL database on Render
2. Copy connection string
3. Add to backend environment variables

### 2. Run Migrations
```bash
# After deployment, run migrations
flask db upgrade

# Seed initial data
python seed.py
```

## Production Checklist

### Security
- [ ] Environment variables set correctly
- [ ] Debug mode disabled
- [ ] CORS configured for production domains
- [ ] JWT secrets are secure
- [ ] M-Pesa credentials are production-ready

### Performance
- [ ] Database indexes created
- [ ] Static assets optimized
- [ ] CDN configured (if needed)
- [ ] Caching headers set

### Monitoring
- [ ] Error tracking configured
- [ ] Performance monitoring enabled
- [ ] Uptime monitoring set up
- [ ] Backup strategy implemented