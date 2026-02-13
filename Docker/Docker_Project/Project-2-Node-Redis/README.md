# Project 2: Node.js + Redis using Docker Compose

This project demonstrates a **multi-container Docker setup** with a **Node.js backend** and a **Redis database**, orchestrated using **Docker Compose**.  
It highlights practical skills in **containerization, backend development, and database caching** — essential for DevOps and full-stack roles.

---

## Features
- Multi-container application setup with Docker Compose  
- Node.js backend server  
- Redis database for caching or session storage  
- Easy orchestration and scaling using Docker Compose  

---

## Tech Stack
- **Node.js** – Backend runtime environment  
- **Redis** – In-memory database for caching  
- **Docker** – Containerization  
- **Docker Compose** – Multi-container orchestration  
- **JavaScript** – Backend logic  

---

## How to Run

1. **Clone the repository**
```bash
git clone <repo-url>
cd DevOps_Concepts/Docker/Docker_Project/Project-2-Node-Redis/
Build and start containers

docker-compose up --build
Access the application

Node.js backend: http://localhost:3000 (or your configured port)

Redis database runs internally in its container, connected to Node.js

Stop containers

docker-compose down

Key Skills Practiced
Docker containerization and networking

Multi-container orchestration using Docker Compose

Integrating backend applications with Redis caching

Environment configuration and scalability

Understanding real-world DevOps workflows

📂 Folder Structure
Project-2-Node-Redis/
├─ Dockerfile
├─ docker-compose.yml
├─ index.js
├─ package.json
└─ README.md
