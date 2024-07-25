class NewServiceConfig:

    # Service Configuration
    SERVICE_NAME= "NewService"
    SERVICE_AUTH_KEY="27b9678d-126a-4096-9b0c-dde992ea6c54"

    # Database Configuration
    DATABASE_URL= "postgresql+asyncpg=//user=password@localhost/dbname"
    DB_USER= "database_user_name"
    DB_PASSWORD= "database_user_password"
    DB_HOST= "database_hostname_url"
    DB_PORT= 10135 #database portnumber 10135 is default, check your database settings to get your port number
    DB_NAME= "database_name"

newserviceconfig = NewServiceConfig()