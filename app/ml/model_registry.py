# app/ml/model_registry.py
"""
Model registry for managing different ML models.
"""


class ModelRegistry:
    """Registry for managing multiple machine learning models."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelRegistry, cls).__new__(cls)
            cls._instance._models = {}
            cls._instance._current_model_name = None
        return cls._instance

    def register_model(self, model_name, model_class):
        """Register a new model with the registry."""
        self._models[model_name] = model_class
        if self._current_model_name is None:
            self._current_model_name = model_name

    def get_model(self, model_name=None):
        """Get a model by name, or the current model if no name is provided."""
        if model_name is None:
            model_name = self._current_model_name

        if model_name not in self._models:
            raise ValueError(f"Model {model_name} is not registered")

        return self._models[model_name]

    def set_current_model(self, model_name):
        """Set the current active model."""
        if model_name not in self._models:
            raise ValueError(f"Model {model_name} is not registered")

        self._current_model_name = model_name

    def get_current_model_name(self):
        """Get the name of the currently active model."""
        return self._current_model_name

    def list_available_models(self):
        """List all available models in the registry."""
        return list(self._models.keys())
