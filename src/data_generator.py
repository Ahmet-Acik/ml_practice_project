"""
Data Generator Module

Creates synthetic datasets for machine learning practice.
Includes various scenarios suitable for GCSE and A-Level learning.
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict, Optional
import os


class DataGenerator:
    """Generate synthetic datasets for ML practice."""
    
    def __init__(self, random_state: int = 42):
        """Initialize with random state for reproducibility."""
        self.random_state = random_state
        np.random.seed(random_state)
    
    def generate_student_performance(self, n_samples: int = 1000) -> pd.DataFrame:
        """
        Generate synthetic student performance data.
        
        Features:
        - study_hours: Hours studied per week
        - attendance: Percentage attendance
        - previous_grade: Previous exam grade (0-100)
        - sleep_hours: Average sleep hours per night
        - extra_activities: Number of extracurricular activities
        - family_support: Family support score (1-5)
        
        Target:
        - exam_score: Final exam score (0-100)
        """
        # Generate base features
        study_hours = np.random.gamma(2, 2, n_samples)  # 0-20 hours
        attendance = np.random.beta(8, 2, n_samples) * 100  # 0-100%
        previous_grade = np.random.normal(65, 15, n_samples)  # Previous performance
        sleep_hours = np.random.normal(7, 1.5, n_samples)  # Sleep hours
        extra_activities = np.random.poisson(2, n_samples)  # Number of activities
        family_support = np.random.randint(1, 6, n_samples)  # Support score
        
        # Ensure realistic ranges
        study_hours = np.clip(study_hours, 0, 40)
        attendance = np.clip(attendance, 0, 100)
        previous_grade = np.clip(previous_grade, 0, 100)
        sleep_hours = np.clip(sleep_hours, 4, 12)
        extra_activities = np.clip(extra_activities, 0, 10)
        
        # Calculate exam score with realistic relationships
        exam_score = (
            0.3 * study_hours +
            0.2 * attendance +
            0.4 * previous_grade +
            0.05 * sleep_hours * 10 +
            0.02 * family_support * 10 -
            0.03 * extra_activities * 5 +
            np.random.normal(0, 5, n_samples)  # Random noise
        )
        
        exam_score = np.clip(exam_score, 0, 100)
        
        # Create DataFrame
        data = pd.DataFrame({
            'student_id': range(1, n_samples + 1),
            'study_hours': study_hours.round(1),
            'attendance': attendance.round(1),
            'previous_grade': previous_grade.round(1),
            'sleep_hours': sleep_hours.round(1),
            'extra_activities': extra_activities,
            'family_support': family_support,
            'exam_score': exam_score.round(1)
        })
        
        # Add some missing values for realistic practice
        missing_indices = np.random.choice(n_samples, int(0.05 * n_samples), replace=False)
        data.loc[missing_indices, 'sleep_hours'] = np.nan
        
        return data
    
    def generate_email_spam(self, n_samples: int = 2000) -> pd.DataFrame:
        """
        Generate synthetic email spam detection data.
        
        Features:
        - email_length: Length of email in characters
        - num_links: Number of links in email
        - num_images: Number of images
        - caps_ratio: Ratio of capital letters
        - exclamation_marks: Number of exclamation marks
        - spam_words: Number of common spam words
        
        Target:
        - is_spam: Binary classification (0=ham, 1=spam)
        """
        # Generate features with different distributions for spam/ham
        is_spam = np.random.binomial(1, 0.3, n_samples)  # 30% spam
        
        # Email length (spam tends to be shorter)
        email_length = np.where(
            is_spam,
            np.random.exponential(200, n_samples),  # Spam: shorter
            np.random.exponential(500, n_samples)   # Ham: longer
        )
        
        # Number of links (spam has more)
        num_links = np.where(
            is_spam,
            np.random.poisson(5, n_samples),  # Spam: more links
            np.random.poisson(1, n_samples)   # Ham: fewer links
        )
        
        # Number of images
        num_images = np.where(
            is_spam,
            np.random.poisson(3, n_samples),  # Spam: more images
            np.random.poisson(0.5, n_samples)  # Ham: fewer images
        )
        
        # Capital letters ratio (spam uses more caps)
        caps_ratio = np.where(
            is_spam,
            np.random.beta(2, 3, n_samples),  # Spam: higher caps ratio
            np.random.beta(1, 9, n_samples)   # Ham: lower caps ratio
        )
        
        # Exclamation marks (spam uses more)
        exclamation_marks = np.where(
            is_spam,
            np.random.poisson(3, n_samples),  # Spam: more exclamations
            np.random.poisson(0.3, n_samples)  # Ham: fewer exclamations
        )
        
        # Spam words count
        spam_words = np.where(
            is_spam,
            np.random.poisson(8, n_samples),  # Spam: more spam words
            np.random.poisson(1, n_samples)   # Ham: fewer spam words
        )
        
        # Ensure realistic ranges
        email_length = np.clip(email_length, 10, 2000)
        num_links = np.clip(num_links, 0, 20)
        num_images = np.clip(num_images, 0, 10)
        exclamation_marks = np.clip(exclamation_marks, 0, 15)
        spam_words = np.clip(spam_words, 0, 20)
        
        data = pd.DataFrame({
            'email_id': range(1, n_samples + 1),
            'email_length': email_length.astype(int),
            'num_links': num_links,
            'num_images': num_images,
            'caps_ratio': caps_ratio.round(3),
            'exclamation_marks': exclamation_marks,
            'spam_words': spam_words,
            'is_spam': is_spam
        })
        
        return data
    
    def generate_sales_forecast(self, n_months: int = 60) -> pd.DataFrame:
        """
        Generate synthetic sales forecasting data.
        
        Features:
        - month: Month number
        - seasonal_factor: Seasonal multiplier
        - marketing_spend: Marketing budget
        - competitor_price: Competitor pricing
        - economic_index: Economic indicator
        
        Target:
        - sales: Monthly sales amount
        """
        months = range(1, n_months + 1)
        
        # Seasonal pattern (higher sales in winter months)
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * np.array(months) / 12)
        
        # Marketing spend (varies monthly)
        marketing_spend = np.random.gamma(2, 1000, n_months)
        
        # Competitor pricing (affects our sales negatively)
        competitor_price = np.random.normal(50, 10, n_months)
        
        # Economic index (affects overall market)
        economic_index = 100 + np.cumsum(np.random.normal(0, 2, n_months))
        
        # Generate sales with trend, seasonality, and noise
        base_sales = 10000  # Base monthly sales
        trend = np.array(months) * 50  # Growing trend
        
        sales = (
            base_sales +
            trend +
            base_sales * (seasonal_factor - 1) +
            0.5 * marketing_spend +
            -100 * (competitor_price - 50) +
            50 * (economic_index - 100) +
            np.random.normal(0, 1000, n_months)  # Random noise
        )
        
        sales = np.clip(sales, 1000, None)  # Ensure positive sales
        
        data = pd.DataFrame({
            'month': months,
            'seasonal_factor': seasonal_factor.round(2),
            'marketing_spend': marketing_spend.round(2),
            'competitor_price': competitor_price.round(2),
            'economic_index': economic_index.round(2),
            'sales': sales.round(2)
        })
        
        return data


def generate_datasets(output_dir: str = "data/raw") -> Dict[str, str]:
    """
    Generate all practice datasets and save to files.
    
    Args:
        output_dir: Directory to save the datasets
        
    Returns:
        Dictionary mapping dataset names to file paths
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    generator = DataGenerator()
    
    # Generate datasets
    datasets = {
        'student_performance': generator.generate_student_performance(1000),
        'email_spam': generator.generate_email_spam(2000),
        'sales_forecast': generator.generate_sales_forecast(60)
    }
    
    # Save datasets
    file_paths = {}
    for name, data in datasets.items():
        file_path = os.path.join(output_dir, f"{name}.csv")
        data.to_csv(file_path, index=False)
        file_paths[name] = file_path
        print(f"Generated {name} dataset: {data.shape[0]} rows, {data.shape[1]} columns")
        print(f"Saved to: {file_path}")
    
    return file_paths


if __name__ == "__main__":
    # Generate datasets when run directly
    print("Generating practice datasets...")
    file_paths = generate_datasets()
    print("\nDatasets generated successfully!")
    print("You can now start with the Jupyter notebooks to explore the data.")
