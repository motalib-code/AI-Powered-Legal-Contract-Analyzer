AI-Powered Legal Contract Analyzer
An intelligent system developed by CothonSolutions for analyzing legal contracts using natural language processing (NLP) and machine learning (ML). This web-based tool automates the extraction of key clauses, identifies risky or unusual clauses, generates plain-English summaries, and provides an interactive dashboard for legal and business professionals.
Features

Text Extraction: Extracts text from PDF and DOCX documents using pdfplumber and docx2txt.
Clause Extraction: Identifies key clauses (e.g., indemnity, confidentiality, governing law) using SpaCy’s Named Entity Recognition (NER).
Risk Classification: Classifies clauses as risky or unusual using machine learning models trained with Scikit-learn.
Contract Summarization: Generates plain-English summaries using HuggingFace’s Legal-BERT.
Interactive Dashboard: Visualizes analysis results with Streamlit and Plotly/Matplotlib.
Data Storage: Stores extracted data in SQLite and manipulates it with Pandas/JSON.

Requirements

Python 3.9 or higher
Required packages (see requirements.txt):
streamlit>=1.31.1
pandas>=2.2.0
plotly>=5.18.0
nltk>=3.8.1
PyPDF2>=3.0.1
pdfplumber>=0.10.3
python-docx>=1.1.0
spacy>=3.6.1
scikit-learn>=1.3.0
transformers>=4.30.2
Additional dependencies listed in setup.py



Installation

Clone the repository:
git clone https://github.com/cothonsolutions/legal-contract-analyzer.git
cd legal-contract-analyzer


Create a virtual environment (recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Install SpaCy model:
python -m spacy download en_core_web_sm


Download required NLTK data:
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_ne_chunker'); nltk.download('words')"



Usage

Start the Streamlit application:
streamlit run src/main.py


Access the web interface:

Open your web browser and navigate to http://localhost:8501 (or the URL shown in the terminal).
Upload a contract document (PDF or DOCX).
View the extracted clauses, risk analysis, summary, and interactive dashboard.



Project Structure
legal-contract-analyzer/
├── src/
│   └── main.py              # Main Streamlit application
├── models/
│   ├── __init__.py
│   ├── ner_model.py         # Named Entity Recognition logic
│   ├── classifier.py        # Clause risk classification
│   └── summarizer.py        # Contract summarization with Legal-BERT
├── extractors/
│   ├── __init__.py
│   ├── pdf_extractor.py     # PDF text extraction
│   └── docx_extractor.py    # DOCX text extraction
├── data/
│   └── database.sqlite      # SQLite database for storing extracted data
├── temp/                    # Temporary file storage
├── logs/
│   └── contract_analyzer.log # Application logs
├── requirements.txt         # Python dependencies
├── setup.py                # Package setup script
└── README.md               # This file

Error Handling
The application includes robust error handling for:

Invalid file types or sizes
Text extraction failures
Model prediction errors
Database operation issues
File upload problems

Logging
Logs are written to logs/contract_analyzer.log, capturing:

Application startup/shutdown
File processing events
Model operations
Error messages

Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Create a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments
Developed by CothonSolutions. Special thanks to the open-source community for providing tools like SpaCy, Scikit-learn, HuggingFace, and Streamlit.
