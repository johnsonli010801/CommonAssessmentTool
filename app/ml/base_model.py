# app/ml/base_model.py
"""
Base model interface for machine learning models.
All model implementations should inherit from this class.
"""
from abc import ABC, abstractmethod
import pickle

class BaseModel(ABC):
    """Abstract base class for all ML models."""
    
    @abstractmethod
    def train(self, features, targets):
        """Train the model with the given features and targets."""
        pass
    
    @abstractmethod
    def predict(self, features):
        """Make predictions using the trained model."""
        pass
    
    @abstractmethod
    def get_name(self):
        """Return the name of the model."""
        pass
    
    def save(self, filename):
        """Save the model to a file."""
        with open(filename, "wb") as model_file:
            pickle.dump(self, model_file)
    
    @classmethod
    def load(cls, filename):
        """Load the model from a file."""
        with open(filename, "rb") as model_file:
            return pickle.load(model_file)