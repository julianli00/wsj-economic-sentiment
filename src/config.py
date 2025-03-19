import os

# Base directory configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Data directory configuration
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
ANNOTATED_DATA_DIR = os.path.join(DATA_DIR, "annotated")
ANALYSIS_DIR = os.path.join(DATA_DIR, "analysis")

# File path configuration
READY_FOR_ANNOTATION_FILE = os.path.join(PROCESSED_DATA_DIR, "ready_for_annotation.csv")
ANNOTATED_DATA_FILE = os.path.join(ANNOTATED_DATA_DIR, "annotated_data.csv")
ANALYSIS_REPORT_FILE = os.path.join(ANALYSIS_DIR, "analysis_report.json")

# Annotator configuration
ANNOTATORS = [
    "X1",
    "X2",
    "X3",
    "X4"
]

# Random seed for reproducibility
RANDOM_SEED = 523
