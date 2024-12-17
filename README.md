# Blog Application

This is a full-stack **Blog Application** built using **React** for the frontend and **Django Rest Framework (DRF)** for the backend.

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Setup and Installation](#setup-and-installation)
   - [Backend Setup](#backend-setup-django-rest-framework)
   - [Frontend Setup](#frontend-setup-react)
5. [Run the Application](#run-the-application)
6. [API Endpoints](#api-endpoints)
7. [Screenshots](#screenshots)

---

## Technologies Used

### Backend:
- Python 3.8+
- Django 4.x
- Django Rest Framework
- SQLite (default, can be replaced with PostgreSQL/MySQL)

### Frontend:
- React 
- Axios for API requests


---

## Features
- **Backend**:
  - RESTful API using DRF.
  - CRUD operations for Blog posts (Create, Read, Update, Delete).
  - User authentication and admin panel.

- **Frontend**:
  - Display blog posts with pagination.
  - Add new blog posts.
  - Edit and delete existing posts.
  - Responsive design with Bootstrap.

---

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **Node.js** and **npm** or **Yarn**
- **Git** (optional, for cloning the repository)

---

## Setup and Installation

### Backend Setup (Django Rest Framework)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   The backend API will run at: **http://127.0.0.1:8000**

### Frontend Setup (React)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```
   Or if using Yarn:
   ```bash
   yarn install
   ```

3. Update API base URL in React code:
   Ensure the API requests point to the Django backend URL:
   ```javascript
   const BASE_URL = 'http://127.0.0.1:8000';
   ```

4. Start the React development server:
   ```bash
   npm start
   ```
   Or with Yarn:
   ```bash
   yarn start
   ```
   The frontend will run at: **http://localhost:3000**

---

## Run the Application
1. Start the **Django server** (backend):
   ```bash
   python manage.py runserver
   ```
2. Start the **React server** (frontend):
   ```bash
   npm start
   ```
3. Open the React application in your browser:
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://127.0.0.1:8000

---

## API Endpoints
Here are the key API endpoints provided by the backend:

| Method | Endpoint             | Description               |
|--------|----------------------|---------------------------|
| GET    | /api/posts/          | Get all blog posts        |
| GET    | /api/posts/<id>/     | Retrieve a single post    |
| POST   | /api/posts/          | Create a new blog post    |
| PUT    | /api/posts/<id>/     | Update an existing post   |
| DELETE | /api/posts/<id>/     | Delete a blog post        |

---
## Admin Username & Password 
#username : admin
#password : password@123
