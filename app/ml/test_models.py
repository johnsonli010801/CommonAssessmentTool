# app/ml/test_models.py
"""
Test script for ML models and model registry.
"""
import numpy as np
from app.ml.model_registry import ModelRegistry
from app.ml.models.random_forest import RandomForestModel
from app.ml.models.gradient_boost import GradientBoostingModel
from app.ml.models.linear_regression import LinearRegressionModel


def test_model_registry():
    """Test the model registry and model switching."""
    print("Testing model registry and model switching...")

    # Create the registry
    registry = ModelRegistry()

    # Register models
    registry.register_model("RandomForest", RandomForestModel())
    registry.register_model("GradientBoosting", GradientBoostingModel())
    registry.register_model("LinearRegression", LinearRegressionModel())

    # List available models
    models = registry.list_available_models()
    print(f"Available models: {models}")

    # Get current model
    current_model_name = registry.get_current_model_name()
    print(f"Current model: {current_model_name}")

    # Switch models
    registry.set_current_model("GradientBoosting")
    print(f"Switched to model: {registry.get_current_model_name()}")

    # Create some dummy data for testing
    features = np.random.rand(10, 31)  # 24 client features + 7 intervention features
    targets = np.random.rand(10)

    # Train all models
    for model_name in models:
        print(f"Training {model_name}...")
        model = registry.get_model(model_name)
        model.train(features, targets)

    # Make predictions with each model
    for model_name in models:
        print(f"Testing predictions with {model_name}...")
        model = registry.get_model(model_name)
        predictions = model.predict(features[:1])
        print(f"  Prediction: {predictions[0]}")

    print("Model testing complete!")


if __name__ == "__main__":
    test_model_registry()
