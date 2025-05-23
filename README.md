# Legal Contract Analyzer

An AI-powered tool for analyzing legal contracts, extracting key clauses, and generating summaries.

## Features

- Named Entity Recognition (NER) for legal entities
- Clause classification and categorization
- Contract summarization
- Risk analysis
- Document metadata extraction
- Support for PDF and DOCX files

## Requirements

- Python 3.9 or higher
- CUDA-capable GPU (optional, for transformer models)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/legal-contract-analyzer.git
cd legal-contract-analyzer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

4. Download required models:
```bash
python -m spacy download en_core_web_sm
```

## Usage

1. Start the web application:
```bash
streamlit run src/main.py
```

2. Train models (optional):
```bash
train-models
```

3. Prepare dataset (optional):
```bash
prepare-dataset
```

## Project Structure

```
legal-contract-analyzer/
├── src/
│   ├── extractors/      # Document extraction modules
│   ├── models/          # AI models
│   ├── database/        # Database management
│   └── main.py         # Main application
├── scripts/
│   ├── run_app.py      # Application runner
│   ├── train_models.py # Model training
│   └── prepare_dataset.py
├── tests/              # Test suite
├── data/              # Dataset directory
├── models/            # Trained models
├── requirements.txt   # Dependencies
└── setup.py          # Package setup
```

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For issues and feature requests, please use the GitHub issue tracker. 

## Reinstall Dependencies

Run the reinstall script to set up a clean environment:
```bash
python scripts/reinstall_deps.py
```

Activate the virtual environment:
```bash
# On Windows:
.\venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

Run the application:
```bash
streamlit run src/main.py
``` 