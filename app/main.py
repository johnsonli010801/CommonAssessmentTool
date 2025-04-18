"""
Main application module for the Common Assessment Tool.
This module initializes the FastAPI application and includes all routers.
Handles database initialization and CORS middleware configuration.
"""

# Related third-party imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Local application/library specific imports
from app.database import engine, Base  # Add Base here
from app.ml.router import router as models_router  # newly added
from app.clients.router import router as clients_router
from app.auth.router import router as auth_router


# Initialize database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="Case Management API",
    description="API for managing client cases",
    version="1.0.0",
)

# Include routers
app.include_router(models_router)
app.include_router(auth_router)
app.include_router(clients_router)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # type: ignore
    allow_methods=["*"],  # type: ignore
    allow_headers=["*"],  # type: ignore
    allow_credentials=True,  # type: ignore
)
