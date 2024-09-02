# FastAPI + PostgreSQL Server Template

## Introduction

Welcome to the **FastAPI + PostgreSQL Server** project template! 🚀 This template is designed to help you quickly get started with building scalable services using FastAPI as the web framework and PostgreSQL as the database.

This project includes a basic setup with a sample service, database connection, and authentication mechanism to demonstrate how to structure your app and add new services.

## Project Overview

In this template, you will find an example of how to use FastAPI to create a service architecture with PostgreSQL database integration and a simple authentication system.

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

   Update the `server/config.py` file with your PostgreSQL credentials:

   ```python
   class AppConfig:
       # App Config
       APP_NAME = "FastAPI Microservices Template"
       APP_ENV = "development"
       APP_HOST = "127.0.0.1"
       APP_PORT = 8000
       APP_AUTH_KEY = "your-auth-key"

       # Database Configuration
       DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"
       DB_USER = "database_user_name"
       DB_PASSWORD = "database_user_password"
       DB_HOST = "database_hostname_url"
       DB_PORT = 5432
       DB_NAME = "database_name"

       # Other Configuration
       DEBUG = True
       LOG_LEVEL = "info"

   config = AppConfig()
   ```

4. **Start the Development Server**

   Start the FastAPI development server:

   ```bash
   python index.py
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the Swagger UI for your API.


### Project Structure

Here’s an overview of the project structure:

```
/server
  /apis.py          # Contains all API endpoints
  /config.py        # Contains configuration settings
  /db.py            # Contains database connection setup for both pg and ORM
  /models.py        # Contains Pydantic models and database operations
  /ormmodels.py    # Contains ORM models and operations using SQLAlchemy
  /index.py         # Contains FastAPI application setup and database initialization
```

### Database Connections

This template supports two types of database connections:

1. **Direct PostgreSQL Connection**

   Use `psycopg2` for direct PostgreSQL database operations. Configure the connection in `db.py`:

   ```python
   import psycopg2
   from server.config import AppConfig

   def get_pg_connection():
       conn = psycopg2.connect(
           dbname=AppConfig.DB_NAME,
           user=AppConfig.DB_USER,
           password=AppConfig.DB_PASSWORD,
           host=AppConfig.DB_HOST,
           port=AppConfig.DB_PORT
       )
       return conn
   ```

   Use `get_pg_connection()` to perform database operations in `models.py`.

2. **ORM-based Connection**

   Use SQLAlchemy for ORM-based database operations. Configure the ORM setup in `db.py`:

   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker
   from server.config import AppConfig

   DATABASE_URL = AppConfig.DATABASE_URL
   engine = create_engine(DATABASE_URL, echo=True)
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base = declarative_base()
   ```

   Define ORM models and operations in `ormmodels.py`.

### Running the Server

To run the FastAPI server with Uvicorn, use the following command:

```bash
uvicorn index:app --host 127.0.0.1 --port 8000 --reload
```

- `index:app` refers to the `app` instance in `index.py`.
- `--reload` enables automatic reloading of the server on code changes.

Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI for your API.

Since there is a router included as well to isolate all the api calls from apis.py when you first setup the server all requests made to apis.py will be in form SERVER_URL/service/your_api_route where /service is the route for apis.py which can be changed by the developer depending on their use case from index.py.

### Authentication

This template includes a basic authentication mechanism using an AUTH_KEY. To access protected endpoints, you need to include the App-Auth-Key header in your requests. Check config.py and apis.py to see how this has been implemented.

## Contributing

If you have suggestions for improvements or find issues, feel free to open an issue or submit a pull request!

## License

This project is licensed under the

 MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any specifics based on your actual implementation details or requirements.