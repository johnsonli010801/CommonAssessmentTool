# app/ml/models/linear_regression.py
"""
Linear Regression implementation for success rate prediction.
"""
from sklearn.linear_model import LinearRegression
from app.ml.base_model import BaseModel

class LinearRegressionModel(BaseModel):
    """Linear Regression model for predicting success rates."""
    
    def __init__(self):
        """Initialize the model."""
        self.model = LinearRegression()
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
        return "LinearRegression"