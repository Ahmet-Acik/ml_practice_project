from setuptools import setup, find_packages

setup(
    name="ml-practice-project",
    version="1.0.0",
    description="Educational Machine Learning Practice Project for GCSE & A-Level Students",
    author="ML Education Team",
    author_email="education@example.com",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
        "jupyter>=1.0.0",
        "streamlit>=1.10.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="machine learning, education, data science, python",
    project_urls={
        "Documentation": "https://github.com/example/ml-practice-project",
        "Source": "https://github.com/example/ml-practice-project",
    },
)
