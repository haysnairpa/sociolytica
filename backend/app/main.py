from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routers
from app.api.v1.endpoints import (
    auth,
    users,
    analytics,
    hashtags,
    sentiment,
    engagement
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(analytics.router, prefix="/api/v1/analytics")
app.include_router(hashtags.router, prefix="/api/v1/hashtags")
app.include_router(sentiment.router, prefix="/api/v1/sentiment")
app.include_router(engagement.router, prefix="/api/v1/engagement")

@app.get("/")
async def root():
    return {"message": "Welcome to Advanced Social Media Analytics Platform API"}
