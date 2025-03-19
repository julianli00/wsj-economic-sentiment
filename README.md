# WSJ Sentiment Annotation and Analysis

This Streamlit-based web application enables users to visualize and analyze sentiment annotations of Wall Street Journal articles.

## Project Structure

```
wsj-corpus-annotation/
├── data/                      # Data files
│   ├── raw/                  # Raw scraped WSJ articles
│   ├── processed/            # Preprocessed data for annotation
│   ├── annotated/            # Annotated data with sentiment scores
│   └── analysis/             # Analysis results and reports
├── docs/                     # Documentation
│   ├── annotation_process.md # Annotation process details
│   ├── annotation_plan.md    # Annotation planning
│   ├── corpus_analysis.md    # Corpus analysis report
│   ├── corpus_readme.md      # Corpus documentation
│   ├── interface_plan.md     # Interface planning
│   ├── interannotator_agreement_study.md  # Agreement analysis
│   ├── proof_of_concept.md   # Initial proof of concept
│   ├── proposal.md           # Project proposal
│   ├── teamwork_contract.md  # Team collaboration guidelines
│   ├── web_code_documentation.md  # Web interface documentation
│   └── wsj_sentiment_annotation_guidelines.md  # Annotation guidelines
├── docker/                   # Docker-related files
│   ├── Dockerfile           # Docker configuration
│   ├── docker-compose.yml        # Docker env
│   ├── .dockerignore        # Docker ignore rules
│   └── DOCKER_SETUP.md      # Docker setup instructions
├── imgs/                     
│   ├── distribution_of_articles_by_category.png             
│   ├── number_of_articles_over_time.png        
├── src/                     # Source code
│   ├── main.py             # Main application entry point
│   ├── scraper.py          # WSJ article scraper
│   ├── data_preprocessing.py # Data preprocessing module
│   ├── agreement_analysis.py # Agreement analysis module
│   ├── args_parser.py       # Command line argument parser
│   └── config.py           # Configuration settings
│   └── app.py              # Interface buliding code
├── tests/                   # Test files
│   ├── src/                # Test source code
│   └── data/               # Test data
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md              # Project documentation
├── environment.yml        # Conda environment specification
└── requirements.txt       # Python package dependencies
```

## Project Documentation

### Sprint 1: Project Setup
- [Proof of concept](docs/proof_of_concept.md)
- [Proposal](docs/proposal.md)
- [Teamwork contract](docs/teamwork_contract.md)
  
### Sprint 2: Data Collection
- [Corpus collection code](src/scraper.py)
- [Corpus + explanation](data/raw/wsj_US_econ_articles_2024-01-01_2025-02-26.csv)
- [Corpus analysis](docs/corpus_analysis.md)
- [Annotation plan](docs/annotation_plan.md)
- [Annotation schema](docs/wsj_sentiment_annotation_guidelines.md)

### Sprint 3: Annotation Process
- [Annotation process details](docs/annotation_process.md)
- [Annotation shared doc](https://docs.google.com/spreadsheets/d/12IgM8detMV0EI2Ba9VFObUoZJfmYE-UMlbuJmKhkY3U/edit?usp=sharing)
- [Data for annotation](data/processed/ready_for_annotation.csv)
- [Annotated data](data/annotated/annotated_data.csv)
- [Interannotator agreement study](docs/interannotator_agreement_study.md)
- [Interface plan](docs/interface_plan.md)

### Sprint 4: Web Interface
- [Web Application](https://huggingface.co/spaces/alexdu271/streamlit_web_annotation_data)
- [Web Documentation](docs/web_code_documentation.md)

## Sprint 5: Docker:
- [Docker File](docker/)

## Features

- Interactive data visualization
- Sentiment distribution analysis
- Annotator agreement study
- Search and filter functionality
- Responsive web interface

## Setup Instructions

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.ubc.ca/yyyuchen/wsj-corpus-annotation.git
cd wsj-corpus-annotation
```

2. Build Docker image:
```bash
docker build -t wsj-annotation-app -f docker/Dockerfile .
```

3. Run the container:
```bash
docker run -p 8501:8501 wsj-annotation-app
```

4. Access the application at http://localhost:8501

### Local Development Setup

1. Create and activate conda environment:
```bash
conda env create -f environment.yml
conda activate wsjenv
```

2. Alternative: Using pip with virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py --mode scrape --start-date 2024-01-01 --end-date 2025-02-26  # For scraping
python src/main.py --mode preprocess --samples 200  # For preprocessing
python src/main.py --mode analyze  # For analysis
```

## Annotation Process

The sentiment annotation process follows these guidelines:

- Positive (1): Headlines indicating market/economic growth, strong performance
- Negative (-1): Headlines suggesting economic risks, market decline
- Neutral (0): Objective descriptions without clear sentiment

Annotation challenges and solutions:
- Mixed sentiment: Labeled neutral unless one aspect clearly dominates
- Policy headlines: Based on implied economic impact
- Economic data: Based on market reaction and expectations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
