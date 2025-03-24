# app/ml/models/random_forest.py
"""
Random Forest implementation for success rate prediction.
"""
from sklearn.ensemble import RandomForestRegressor
from app.ml.base_model import BaseModel

class RandomForestModel(BaseModel):
    """Random Forest model for predicting success rates."""
    
    def __init__(self, n_estimators=100, random_state=42):
        """Initialize the model with parameters."""
        self.model = RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=random_state
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
        return "RandomForest"