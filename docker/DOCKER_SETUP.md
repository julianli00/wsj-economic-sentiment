# WSJ Article Annotation Visualization - Docker Setup

This document provides instructions for running the WSJ Article Annotation Visualization application using Docker.

## Prerequisites

Before you begin, ensure you have:
- Docker installed
- At least 2GB of free memory
- Internet connection

## Quick Start

1. Open terminal and navigate to the project directory
2. Run the following command to start the application:
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```
3. Once you see the following output, the application is ready:
   ```
   You can now view your Streamlit app in your browser.
   URL: http://0.0.0.0:8501
   ```
4. Open your browser and visit: http://localhost:8501

## Testing Guide

Please test the following features:

### 1. Data Browser
- Use the search box to search for specific articles
  - Try keywords like "Fed", "Economy", "Markets"
  - Try searching for dates (e.g., "2024")
- Navigate through different pages using the page number input
- Check if the data table displays correctly with all columns

### 2. Data Visualization
- Check the Annotation Distribution bar chart
  - Verify the distribution of positive, negative, and neutral annotations
  - Compare annotations between annotators
- Verify the Agreement Rate percentage
- Examine the Agreement/Disagreement pie chart
- Look at the random sample data at the bottom

## Troubleshooting

If you encounter any issues:

1. Port Conflict
   - Make sure port 8501 is not being used by another application
   - If needed, you can modify the port in docker-compose.yml

2. Docker Issues
   - Try rebuilding the container:
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```

## Project Structure

```
.
├── docker/
│   ├── Dockerfile           # Docker image configuration
│   ├── docker-compose.yml   # Docker compose configuration
│   └── DOCKER_SETUP.md      # This setup guide
├── src/
│   └── app.py              # Streamlit application code
└── data/
    └── annotated/
        └── annotated_data.csv  # Annotation data
```

## Expected Output

When the application starts successfully, you should see:
```
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.

You can now view your Streamlit app in your browser.
URL: http://0.0.0.0:8501
```

The web interface will display:
1. A sidebar with page selection options
2. Data browser with search functionality
3. Data visualization with interactive charts
4. Sample data display 