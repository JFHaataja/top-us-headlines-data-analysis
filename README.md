# 📢 Top US News Headlines Fetcher & Data Analysis

This repository consists of two main files: **top-headlines.py** and **top-us-headlines-analysis.ipynb**.  

The first main file (top-headlines.py) consists of a **Python** script that fetches the latest US news
headline data from the [NewsAPI](https://newsapi.org/) and saves them to an Excel file (top_headlines.xlsx).  

The the second main file (top-us-headlines-analysis.ipynb) is a Jupyter notebook which analyzes news headlines
from the United States, collected via the NewsAPI. The data is preprocessed, analyzed, and visualized to gain
insights into news trends. The analyzed data is then saved to a new Excel file (analyzed_headlines.xlsx).

## 🛠️ Installation
### top-headlines.py:
1. Install the required libraries:  

   ```python
      pip install requests pandas openpyxl
   ```
   
2. Create a config.py file and add your API key:

   ```python
      API_KEY = "YOUR_NEWSAPI_KEY"
   ```
   
3. Run the script:
   ```python
      python script.py
   ```
### top-us-headlines-analysis.ipynb:

1. Install the required libraries:

   ```python
      pip install numpy pandas matplotlib seaborn textblob scikit-learn openpyxl
   ```
Also, make sure the dataset `top_headlines.xlsx` is available in the same directory as the notebook.
