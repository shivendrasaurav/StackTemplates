# Use this file if NewService has to be run as standalone service

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.newservice.endpoints import router as newservice_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
  

# Include the service router
app.include_router(newservice_router, prefix="/newservice")

# Add more routers or configurations if needed
