import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")  # Retrieve API key from environment variable
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
FUNCTION_OPTION = "TIME_SERIES_DAILY"

# Fetch stock data
parameters = {
    "function": FUNCTION_OPTION,
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    "datatype": "json"
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_data = response.json()
print(stock_data)

# Get yesterday's and the day before yesterday's closing prices
data = stock_data.get('Time Series (Daily)', {})
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data.get("4. close")

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday.get("4. close")

# Calculate positive difference and difference percentage
positive_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (positive_difference / float(yesterday_closing_price)) * 100

print("Positive Difference:", positive_difference)
print("Difference Percentage:", diff_percent)

# ---------------------------------------------------STOCK NEWS SECTION---------------------------------------------------#

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_api_key = os.getenv("NEWS_API_KEY")  # Retrieve News API key from environment variable
news_response = requests.get(url=f"{NEWS_ENDPOINT}?q=tesla&from=2024-03-07&sortBy=publishedAt&apiKey={news_api_key}")
news_data = news_response.json()['articles']

print(news_data)

# Use a loop to extract the descriptions of the first three articles
three_articles = [article['description'] for article in news_data[:3]]

# if diff_percent >= 5:
#     print(three_articles)

three_headlines = [headline['title'] for headline in news_data[:3]]
print(three_headlines)
