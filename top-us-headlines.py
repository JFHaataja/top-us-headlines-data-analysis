import requests
import pandas as pd
from config import API_KEY

# Defining the parameters
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'country': 'us',  # USA
    'pageSize': 100,   # The number of news we want to retrieve (100 being the max number with the free version)
    'apiKey': API_KEY
}

# Sending the API request
response = requests.get(url, params=params)

# Checking the answer
if response.status_code == 200:
    # parsing the answer
    data = response.json()
    
    # Creating a list of the articles for the dataframe
    articles = []
    for article in data.get('articles', []):
        articles.append({
            "Title": article['title'],
            "Source": article['source']['name'],
            "Author": article['author'],
            "Published At": article['publishedAt'],
            "URL": article['url']
        })

    # Converting the list into a dataframe
    df = pd.DataFrame(articles)

    # Saving the article data into an Excel file
    excel_file = 'top_headlines.xlsx'
    df.to_excel(excel_file, index=False, engine='openpyxl')
    print(f"Excel file '{excel_file}' was created successfully!")
else:
    print(f"Error: {response.status_code}, {response.text}")
