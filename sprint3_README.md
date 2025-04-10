# 🌐 Public API Access - Common Assessment Tool

Welcome! This backend application is deployed to the cloud and is publicly accessible so you can explore and test its features using Swagger documentation.

---

## ✅ Access the API

You can access the backend API and test its endpoints using the Swagger UI at the following link:

🔗 **Swagger Documentation**  
[http://ec2-52-32-214-215.us-west-2.compute.amazonaws.com:8000/docs](http://ec2-52-32-214-215.us-west-2.compute.amazonaws.com:8000/docs)

This interface allows you to:
- View all available API endpoints
- Try them out directly in the browser
- See responses and sample inputs

---

## 💡 About This Deployment

- The backend application is deployed on **AWS EC2** as part of a student cloud deployment.
- The service is always online and accessible via the link above.
- No login or credentials are required to use the Swagger interface.

---

## 🎯 Experience

This deployment aims to provide the same user experience as this example:  
[http://ec2-34-219-155-200.us-west-2.compute.amazonaws.com:8000/docs](http://ec2-34-219-155-200.us-west-2.compute.amazonaws.com:8000/docs)

Feel free to explore the endpoints, submit requests, and view real-time responses!

## 🚀 Story 2: Automated Deployment to Public Endpoint (CI/CD)

### 🧩 Story

As a developer, I want to automate the deployment of the backend application to the public endpoint so that my team can easily and quickly make new releases.

---

### ✅ Acceptance Criteria

1. Continuous Deployment (CD) pipeline is built using GitHub Workflows  
2. Upon every Release, which is created from `main`, the CD pipeline should run and automatically update the public endpoint with the new code changes

---

### ⚙️ CI/CD Implementation Summary

- A `cd.yml` GitHub Actions workflow was created to **automate testing and deployment**
- The pipeline runs on:
  - **Every push** to `main`
  - **Every release** created from `main`

---

### 🧪 Pipeline Steps

1. **Checkout Code**  
   The latest version of the backend is pulled into the GitHub Actions runner.

2. **Run Tests**  
   Using `pytest` to ensure code passes before deployment.

3. **SSH into AWS EC2 Instance**  
   Secure SSH connection is made using a GitHub Secret (`EC2_SSH_PRIVATE_KEY`) and public EC2 host (`EC2_HOST`).

4. **Pull New Code on EC2**  
   Runs `git pull origin main` to get the latest updates on the remote server.

5. **Stop the Previous API Server**  
   Uses `pkill uvicorn` to stop any previously running instance.

6. **Start New API Version in the Background**  
   Runs:
   ```bash
   nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > app.log 2>&1 &
