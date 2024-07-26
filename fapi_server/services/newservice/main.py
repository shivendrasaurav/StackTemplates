# Use this file if NewService has to be run as standalone service

from fastapi import FastAPI
from services.newservice.endpoints import router as newservice_router

app = FastAPI()

# Include the service router
app.include_router(newservice_router, prefix="/newservice")

# Add more routers or configurations if needed
