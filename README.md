# FastAPI + PostgreSQL Microservice Template

## Introduction

Welcome to the **FastAPI + PostgreSQL Microservice** project template! 🚀 This template is designed to help you quickly get started with building scalable microservices using FastAPI as the web framework and PostgreSQL as the database.

This project includes a basic setup with a sample microservice, database connection, and authentication mechanism to demonstrate how to structure your app and add new services.

## Project Overview

In this template, you will find an example of how to use FastAPI to create a microservice architecture with PostgreSQL database integration and a simple authentication system.

### Key Features

- **FastAPI** for building high-performance APIs
- **PostgreSQL** integration for robust data storage
- Microservice architecture setup
- Basic authentication mechanism
- Example service with user management operations

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

- [Python](https://www.python.org/) (v3.7 or later)
- [PostgreSQL](https://www.postgresql.org/)
- [Git](https://git-scm.com/)

### Installation

1. **Fetch the template from Repository**

   Follow these `git` commands to set up your project with this template:

   a. Create a folder for your project and navigate into it:
   ```bash
   mkdir {projectName}
   cd {projectName}
   ```

   b. Initialize Git and add template as remote: 
   ```bash
   git init
   git remote add template https://github.com/shivendrasaurav/StackTemplates.git
   ```

   c. Fetch the template and pull the latest code from the `fastapi-postgres` branch:
   ```bash
   git fetch template
   git pull template fastapi-postgres
   ```

   d. Remove the template remote and add your own project's remote with a suitable remote name:
   ```bash
   git remote remove template
   git remote add {remoteName} {gitURL}
   ```

2. **Install Dependencies**

   Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Database**

   Update the database configuration in `server/services/newservice/config.py` with your PostgreSQL credentials.

4. **Start the Development Server**

   Start the FastAPI development server:

   ```bash
   python server/main.py
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the Swagger UI for your API.

## Project Structure

Here's an overview of the project structure:

```
/server
  /services
    /newservice
      apis.py      # contains all API endpoints
      config.py    # contains config related to the current service
      db.py        # contains database connection method and database execution queries
      main.py      # contains FastAPI runner if someone wants to run a service as standalone service
      models.py    # contains data models used by APIs and Database Queries
  config.py        # contains config related to or usable for whole project
  main.py          # contains FastAPI runner for the whole project and its services
```

### Configuration

- **`server/config.py`**: Contains global configuration for the entire application.
- **`server/services/newservice/config.py`**: Contains configuration specific to the `newservice` microservice.

### Main Application

The `server/main.py` file configures the main FastAPI application and includes routers from different services:

```python
from fastapi import FastAPI
from config import config
from services.newservice.apis import router as newservice_router

app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)

# Include routers from different services
app.include_router(newservice_router, prefix="/newservice")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI microservice!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT, log_level=config.LOG_LEVEL)
```

### Models

The `models.py` file defines Pydantic models for request/response schemas and SQLAlchemy models for database operations:

```python
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
```

### Database Operations

The `db.py` file contains functions for database connections and operations:

```python
import psycopg2
from .config import newserviceconfig

def get_db_conn():
    conn = psycopg2.connect(
        dbname=newserviceconfig.DB_NAME,
        user=newserviceconfig.DB_USER,
        password=newserviceconfig.DB_PASSWORD,
        host=newserviceconfig.DB_HOST,
        port=newserviceconfig.DB_PORT
    )
    return conn

def create_user(name: str, email: str):
    # Execute queries and return results

def get_user(user_id: int):
    # Execute queries and return results
```

### API Endpoints

The `apis.py` file defines the API endpoints for the microservice:

```python
from fastapi import APIRouter, Depends, HTTPException, Header
from .config import newserviceconfig
from .db import get_db_conn, create_user, get_user
from .models import UserBase, UserCreate, UserResponse

router = APIRouter()
AUTH_KEY = newserviceconfig.SERVICE_AUTH_KEY

# API endpoints for user management
@router.get("/getauthtoken/")
async def get_auth_key():
    return {"auth_key": AUTH_KEY}

@router.get("/createnewuser/")
async def create_new_user(auth_key: str = Depends(get_token_from_header)):
    # Implementation for creating a new user

@router.get("/getuserwithid/{userid}")
async def get_user_data(userid: int, auth_key: str = Depends(get_token_from_header)):
    # Implementation for getting user data
```

## Adding a New Microservice

To add a new microservice, follow these steps:

1. Create a new directory under `server/services/` for your service.
2. Create the necessary files (`apis.py`, `config.py`, `db.py`, `main.py`, `models.py`) in the new service directory.
3. Update the `server/main.py` file to include the router for your new service.

## Authentication

This template includes a basic authentication mechanism using an `AUTH_KEY`. To access protected endpoints, you need to include the `Service-Auth-Key` header in your requests.

## Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Contributing

If you have suggestions for improvements or find issues, feel free to open an issue or submit a pull request!

## License

This project is licensed under the [MIT License](LICENSE).

---

This README provides a comprehensive guide for users to understand the purpose of the project, how to get started, and how to work with the FastAPI + PostgreSQL microservice template. It includes information about the project structure, configuration, database operations, API endpoints, and instructions for adding new microservices.