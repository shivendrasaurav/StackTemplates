# main.py

from fastapi import FastAPI
from config import config
from fastapi.middleware.cors import CORSMiddleware

from services.newservice.apis import router as newservice_router

# from services.other_service.api import router as other_router

app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)

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

# Include routers from different services
app.include_router(newservice_router, prefix="/newservice")
# app.include_router(other_router, prefix="/other")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI microservice!"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT, log_level=config.LOG_LEVEL)
