# app/ml/data_processor.py
"""
Data processing module for machine learning models.
Handles loading and preprocessing data for model training and prediction.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class DataProcessor:
    """Handles data loading and preprocessing for ML models."""

    def __init__(self, data_file="data_commontool.csv"):
        """Initialize with the data file path."""
        self.data_file = data_file
        self.feature_columns = [
            "age",
            "gender",
            "work_experience",
            "canada_workex",
            "dep_num",
            "canada_born",
            "citizen_status",
            "level_of_schooling",
            "fluent_english",
            "reading_english_scale",
            "speaking_english_scale",
            "writing_english_scale",
            "numeracy_scale",
            "computer_scale",
            "transportation_bool",
            "caregiver_bool",
            "housing",
            "income_source",
            "felony_bool",
            "attending_school",
            "currently_employed",
            "substance_use",
            "time_unemployed",
            "need_mental_health_support_bool",
        ]
        self.intervention_columns = [
            "employment_assistance",
            "life_stabilization",
            "retention_services",
            "specialized_services",
            "employment_related_financial_supports",
            "employer_financial_supports",
            "enhanced_referrals",
        ]

    def load_data(self):
        """Load the dataset from file."""
        return pd.read_csv(self.data_file)

    def prepare_training_data(self):
        """Prepare features and targets for model training."""
        data = self.load_data()
        all_features = self.feature_columns + self.intervention_columns

        features = np.array(data[all_features])
        targets = np.array(data["success_rate"])

        features_train, features_test, targets_train, targets_test = train_test_split(
            features, targets, test_size=0.2, random_state=42
        )

        return features_train, features_test, targets_train, targets_test

    def prepare_prediction_data(self, client_data, interventions):
        """Prepare a single client's data for prediction."""
        # Extract client features from the client data
        client_features = [client_data.get(col, 0) for col in self.feature_columns]

        # Add intervention features
        intervention_features = [
            interventions.get(col, 0) for col in self.intervention_columns
        ]

        # Combine all features
        all_features = client_features + intervention_features

        return np.array([all_features])
