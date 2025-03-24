# app/ml/__init__.py
"""
Machine learning package initialization.
"""
from app.ml.model_registry import ModelRegistry
from app.ml.models.random_forest import RandomForestModel
from app.ml.models.gradient_boost import GradientBoostingModel
from app.ml.models.linear_regression import LinearRegressionModel

# Initialize the model registry with available models
def initialize_models():
    """Register all available models with the registry."""
    registry = ModelRegistry()
    
    # Register the models
    registry.register_model("RandomForest", RandomForestModel())
    registry.register_model("GradientBoosting", GradientBoostingModel())
    registry.register_model("LinearRegression", LinearRegressionModel())
    
    # Set the default model
    registry.set_current_model("RandomForest")
    
    return registry

# Initialize models when importing this package
registry = initialize_models()