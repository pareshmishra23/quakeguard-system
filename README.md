# 🌍 QuakeGuard System

A full-stack earthquake detection and alert system combining mobile sensors, machine learning, and real-time communication.

---

## 🧩 Project Structure

quakeguard-system/
├── mobile-app/ # React Native App (sensors + alerts)
├── backend-api/ # FastAPI Backend API
├── ml-training/ # ML training pipeline (TensorFlow)
├── docker-configs/ # Docker, NGINX, Prometheus configs
├── database/ # DB schema, migrations, seeders
├── scripts/ # Automation: setup, deploy, backup
├── docs/ # API, testing, deployment docs
└── .vscode/ # Debugging & task configs

---

## 🚀 Features

- 📱 Real-time earthquake detection using mobile sensors
- 🧠 On-device ML inference using accelerometer + gyroscope
- 🌐 WebSocket push alerts and API reporting
- 🔐 JWT-based authentication + device verification
- 📊 Prometheus & Grafana monitoring
- 🐳 Dockerized microservice deployment

---

## 📦 Tech Stack

| Layer         | Tools Used                         |
|---------------|------------------------------------|
| Frontend (Mobile) | React Native, Android/iOS Sensors |
| Backend (API)     | FastAPI, Uvicorn, SQLAlchemy     |
| ML Pipeline       | TensorFlow, NumPy, Pandas        |
| Auth & DB         | JWT, PostgreSQL, Firebase (optional) |
| DevOps            | Docker, NGINX, Prometheus, Grafana |
| CI/CD             | GitHub Actions (planned)         |

---

## ⚙️ Setup Instructions

### 🧱 Prerequisites

- Node.js & npm
- Python 3.9+
- Android Studio / Xcode (for mobile)
- Docker & Docker Compose

---

### 📱 Mobile App

```bash
cd mobile-app/QuakeGuardApp
npm install
npx react-native run-android
# or
npx react-native run-ios

cd backend-api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Visit: http://localhost:8000/docs

🤖 ML Training
cd ml-training/src
python model.py

🐳 Docker (All Services)
 
cd docker-configs
docker-compose up --build
🧪 Testing
 
cd scripts
bash
test.sh

---
📄 Documentation
API Reference
Deployment Guide
Security Best Practices

🛡 License
MIT License © 2025 QuakeGuard Team

🙌 Contributors
Paresh Mishra  – Founder, Architect, Developer
