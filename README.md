# SecureFlix

SecureFlix is a Django-based movie streaming platform deployed using Docker on AWS EC2.

## Features

- User Authentication
- Admin Dashboard
- Movie Streaming Platform
- Dockerized Deployment
- NGINX Reverse Proxy
- Rate Limiting for Security
- AWS EC2 Deployment
- Private Subnet Architecture

## Technologies Used

- Django
- Docker
- NGINX
- AWS EC2
- SQLite / MySQL
- Gunicorn

## Docker Setup

### Build Docker Image

```bash
docker build -t secureflix .
```

### Run Docker Container

```bash
docker run -p 9000:8000 secureflix
```

## Security Features

- NGINX Rate Limiting
- Bastion Host Access
- Private Subnet Deployment
- Reverse Proxy Configuration

## Architecture

User → Bastion Host → Private EC2 → Docker → Django

## Author

Sheen Sony m
