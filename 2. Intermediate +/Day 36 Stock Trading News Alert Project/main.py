import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

N_API_KEY = "97d4286d5c094ed985f903cd6e586577"
S_API_KEY = 'H7251RBS0NQ4QKDC'

stock_params = {
    "apikey": S_API_KEY,
    "function": 'TIME_SERIES_DAILY_ADJUSTED',
    "symbol": STOCK_NAME,
    "outputsize": 'compact'
}


news_params = {
    "apiKey": N_API_KEY,
    "q": COMPANY_NAME,
    }

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]


# 1. When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#First we get yesterday's closing stock price using list comprehensions 
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_closing = float(yesterday["4. close"])

# We get the day before yesterday's closing stock price
b4_yesterday = data_list[1]
b4_yesterday_closing = float(b4_yesterday["4. close"])

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff = yesterday_closing - b4_yesterday_closing

symbol = None
if diff > 0:
    symbol =  "🔺"
elif diff < 0:
    symbol = "🔻"


diff_percent = abs(diff) / yesterday_closing * 100

#If percentage is greater than 5 then we print the three latest news of our company
if diff_percent > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # slice to create a list that contains the first 3 articles
    three_articles = articles[0:3]
    print(f'{STOCK_NAME}:{symbol}{diff_percent}%')
    for article in three_articles:
        print(f"Headline: {article['title']} \nBrief: {article['description']} \n")


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

