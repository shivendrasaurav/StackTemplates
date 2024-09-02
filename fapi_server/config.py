class AppConfig:
    # App Config
    APP_NAME = "FastAPI Microservices Template"
    APP_ENV = "development"
    APP_HOST = "127.0.0.1"
    APP_PORT = 8000
    APP_AUTH_KEY = "27b9678d-126a-4096-9b0c-dde992ea6c54"

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
