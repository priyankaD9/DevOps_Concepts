

# Docker Containerization Projects

A hands-on Docker project repository demonstrating **containerization, multi-container orchestration, and DevOps fundamentals** using real applications.
Ideal for beginners and aspiring DevOps engineers to showcase **Docker, Docker Compose, and container-based workflows**.

---

## Project Overview

This repository contains **two Docker-based projects** along with a Docker setup guide, focusing on real-world container usage instead of just commands.

---

### Dockerized Python Application

 **project-1-python-app**

This project demonstrates how to **containerize a Python application** using Docker.

**Features:**

* Simple Python application
* Dockerfile for building a custom image
* Runs the app inside an isolated container
* Ensures consistency across environments

**Automation / Usage:**

* Build the Docker image
* Run the container using Docker CLI

---

### 1Node.js + Redis Application (Docker Compose)

 **Project-2-Node-Redis**

This project demonstrates a **multi-container application** using Docker Compose.

**Features:**

* Node.js application container
* Redis service container
* `docker-compose.yml` to manage both services
* Internal Docker networking between services

**Automation / Usage:**

* Start all services with a single command
* Clean service orchestration using Docker Compose

---

## Skills Demonstrated

* Docker installation and setup
* Writing Dockerfiles
* Containerizing applications
* Docker image creation and container execution
* Multi-container orchestration using Docker Compose
* Container networking basics
* DevOps and cloud-ready fundamentals

---

## Docker Setup & Verification

📄 **DOCKER_SETUP.md**

Includes:

* Docker installation steps
* Verification commands
* Basic Docker health checks

---

## How to Run the Projects

```bash
# Run Python Docker project
docker build -t python-app .
docker run python-app

# Run Node.js + Redis project
docker-compose up
```

---

## Why This Project Matters

This project focuses on **practical Docker usage**, similar to real DevOps workflows:

* Build once, run anywhere
* Service-based architecture
* Clean and reproducible environments

---





Learning Docker becomes powerful when you build real projects 🚀
