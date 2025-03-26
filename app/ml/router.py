# app/ml/router.py
"""
Router for ML model management endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.ml.model_registry import ModelRegistry

router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}},
)


class ModelResponse(BaseModel):
    """Response model for model endpoints."""

    name: str


class ModelsListResponse(BaseModel):
    """Response model for listing available models."""

    models: list[str]
    current_model: str


@router.get("/current", response_model=ModelResponse)
async def get_current_model():
    """Get the currently active model."""
    registry = ModelRegistry()
    current_model = registry.get_current_model_name()
    return {"name": current_model}


@router.get("/available", response_model=ModelsListResponse)
async def list_available_models():
    """List all available models."""
    registry = ModelRegistry()
    available_models = registry.list_available_models()
    current_model = registry.get_current_model_name()
    return {"models": available_models, "current_model": current_model}


@router.post("/switch/{model_name}", response_model=ModelResponse)
async def switch_model(model_name: str):
    """Switch to a different model."""
    registry = ModelRegistry()

    try:
        registry.set_current_model(model_name)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail=f"Model '{model_name}' not found. Available models: {registry.list_available_models()}",
        )

    return {"name": model_name}
