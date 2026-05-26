# 🎬 SecureFlix

A Netflix-inspired OTT streaming platform built with Django and deployed 
on AWS following DevSecOps best practices.

## 🌐 Live Demo
https://d1fnls6126mesp.cloudfront.net

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django (Python) |
| Web Server | Nginx + Gunicorn |
| Database | AWS RDS MySQL |
| Storage | AWS S3 |
| CDN | AWS CloudFront |
| Load Balancer | AWS ALB |
| Containerization | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Monitoring | AWS CloudWatch |

## 🏗️ Architecture
Internet → CloudFront CDN → ALB → EC2 (Nginx → Gunicorn → Django) → RDS MySQL
↓
S3 (static/media)

## 🔒 Security Features

- EC2 in private subnet (no direct internet access)
- firewalld: HTTP only from ALB subnets (10.0.1.0/24, 10.0.5.0/24)
- Nginx rate limiting (5 req/min on login, 100 req/min general)
- Security headers (HSTS, CSP, X-Frame-Options, nosniff)
- SSH hardening + fail2ban
- Automated backups with cron
- Log rotation
- CloudWatch alarms (CPU, memory, disk)

## ⚙️ Local Setup

### Prerequisites
- Python 3.11+
- MySQL
- Docker & Docker Compose

### 1. Clone the repo
```bash
git clone https://github.com/sheensonym/secureflix.git
cd secureflix
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your values
```

### 4. Run migrations and start
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

### 5. Run with Docker
```bash
docker-compose up --build
```

## 🚀 Deployment (AWS)

Push to main branch — GitHub Actions will automatically:
1. Run tests
2. SSH into EC2
3. Pull latest code
4. Restart Gunicorn

## 📁 Project Structure
secureflix/
├── secureflix/          # Django project (settings, urls, wsgi)
├── templates/           # HTML templates
├── static/              # Static files
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/workflows/   # CI/CD pipeline

:wq
