"""
ML Practice Project - Educational Machine Learning Package

This package provides tools and utilities for learning machine learning
concepts step by step, designed for GCSE and A-Level students.
"""

__version__ = "1.0.0"
__author__ = "ML Education Team"

# Import main modules for easy access
from .data_generator import generate_datasets
from .preprocessing import DataPreprocessor
from .models import MLModelTrainer
from .evaluation import ModelEvaluator
from .visualization import DataVisualizer

__all__ = [
    "generate_datasets",
    "DataPreprocessor", 
    "MLModelTrainer",
    "ModelEvaluator",
    "DataVisualizer"
]
