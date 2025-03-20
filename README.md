# 📢 Top US News Headlines Fetcher & Data Analysis

This repository consists of two main files: **top-headlines.py** and **top-us-headlines-analysis.ipynb**.  

The first main file (top-headlines.py) consists of a **Python** script that fetches the latest US news
headline data from the [NewsAPI](https://newsapi.org/) and saves them to an Excel file.  

The the second main file (top-us-headlines-analysis.ipynb) is a Jupyter notebook which analyzes news headlines
from the United States, collected via the NewsAPI. The data is preprocessed, analyzed, and visualized to gain
insights into news trends.

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

## 📝 How Does It Work?

### top-headlines.py:
🔹 **Defines the API URL and parameters**, such as the number of news articles and the country.  
🔹 **Sends an HTTP GET request** using the requests library.  
🔹 **Checks if the response is successful** (HTTP 200).  
🔹 **Parses the JSON data** and extracts relevant information from the news articles.  
🔹 **Converts the extracted data into a Pandas DataFrame** and saves it to an Excel file.  

### top-us-headlines-analysis.ipynb:
**1. Data Preprocessing**  
      🔹 Loads the dataset from top_headlines.xlsx  
      🔹 Checks for duplicates and handling missing values  
      🔹 Cleans URLs by removing placeholder links  
      🔹 Normalizes author names (capitalization)
      
**2. Basic Analysis**  
      🔹 Analyzes news sources (distribution of sources)  
      🔹 Identifies publishing patterns (distribution of publishing days)  
      
**3. Text Analysis**  
      🔹 Finds common keywords in news headlines  
      🔹 Performs sentiment analysis on headlines  
      
**4. Data Visualization**  
      🔹 Creates a pie chart of the top 5 news sources  
      🔹 Creates a line plot showing the daily number of publications  
      
**5. Exporting Analyzed Data**  
      🔹 Saves the cleaned and analyzed data as `analyzed_headlines.xlsx`  
