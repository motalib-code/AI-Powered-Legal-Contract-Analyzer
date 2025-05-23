from setuptools import setup, find_packages

setup(
    name="legal-contract-analyzer",
    version="0.1.0",
    description="AI-powered tool for analyzing legal contracts",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/legal-contract-analyzer/legal-contract-analyzer",
    packages=find_packages(),
    install_requires=[
        "numpy==1.24.3",
        "pandas==2.0.3",
        "scikit-learn==1.3.0",
        "spacy==3.6.1",
        "torch==2.0.1",
        "transformers==4.30.2",
        "streamlit==1.24.0",
        "plotly==5.15.0",
        "python-docx==0.8.11",
        "PyPDF2==3.0.1",
        "joblib==1.3.1",
        "python-dateutil==2.8.2",
        "pytz==2023.3",
        "tqdm==4.65.0",
        "requests==2.31.0",
        "urllib3==2.0.4",
        "certifi==2023.7.22",
        "charset-normalizer==3.2.0",
        "idna==3.4",
        "packaging==23.1",
        "typing-extensions==4.7.1",
        "docx2txt==0.8",
        "matplotlib==3.8.2",
        "sqlalchemy==2.0.27",
        "python-dotenv==1.0.0",
        "beautifulsoup4==4.12.2",
        "nltk==3.8.1",
    ],
    extras_require={
        "dev": [
            "black==24.2.0",
            "flake8==7.0.0",
            "pytest==8.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "contract-analyzer=scripts.run_app:main",
            "train-models=scripts.train_models:main",
            "prepare-dataset=scripts.prepare_dataset:main",
        ]
    },
    python_requires=">=3.9",
)