# Kubernetes Project 3.1 – Nginx Deployment & Scaling

## Overview
This project demonstrates deploying and scaling a containerized Nginx application using Kubernetes.

## Tech Stack
- Kubernetes
- Docker
- kubectl

## Steps to Run
1. Enable Kubernetes in Docker Desktop
2. Apply deployment and service files:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

## Features
- Nginx app deployment using Kubernetes Deployment
- Service exposure using NodePort
- Horizontal pod scaling

## Resources

For more details on Kubernetes architecture and concepts, refer to the official docs:  
(https://kubernetes.io/docs/concepts/architecture/)

