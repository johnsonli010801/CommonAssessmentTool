# app/ml/models/gradient_boost.py
"""
Gradient Boosting implementation for success rate prediction.
"""
from sklearn.ensemble import GradientBoostingRegressor
from app.ml.base_model import BaseModel


class GradientBoostingModel(BaseModel):
    """Gradient Boosting model for predicting success rates."""

    def __init__(self, n_estimators=100, learning_rate=0.1, random_state=42):
        """Initialize the model with parameters."""
        self.model = GradientBoostingRegressor(
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            random_state=random_state,
        )
        self.is_trained = False

    def train(self, features, targets):
        """Train the model with the given features and targets."""
        self.model.fit(features, targets)
        self.is_trained = True
        return self

    def predict(self, features):
        """Make predictions using the trained model."""
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        return self.model.predict(features)

    def get_name(self):
        """Return the name of the model."""
        return "GradientBoosting"
