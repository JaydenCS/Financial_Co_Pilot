import requests
from config import ALPHA_KEY

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = ALPHA_KEY

# Base URL for Alpha Vantage API
BASE_URL = 'https://www.alphavantage.co/query'

# Function to make API calls
def time_series_daily(symbol):
    params = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def time_series_intraday(symbol, interval):
    params = {'function': 'TIME_SERIES_INTRADAY', 'symbol': symbol, 'interval': interval, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def time_series_weekly(symbol):
    params = {'function': 'TIME_SERIES_WEEKLY', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def time_series_monthly(symbol):
    params = {'function': 'TIME_SERIES_MONTHLY', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def quote_endpoint(symbol):
    params = {'function': 'GLOBAL_QUOTE', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def search_endpoint(keywords):
    params = {'function': 'SYMBOL_SEARCH', 'keywords': keywords, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_time_series_adjusted_volume(symbol):
    params = {'function': 'TIME_SERIES_DAILY_ADJUSTED', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_company_overview(symbol):
    params = {'function': 'OVERVIEW', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_earnings(symbol):
    params = {'function': 'EARNINGS', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_income_statement(symbol):
    params = {'function': 'INCOME_STATEMENT', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_balance_sheet(symbol):
    params = {'function': 'BALANCE_SHEET', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_cash_flow(symbol):
    params = {'function': 'CASH_FLOW', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_latest_news(symbol):
    params = {'function': 'LATEST_NEWS', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_news_sentiment(symbol):
    params = {'function': 'NEWS_SENTIMENT', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_social_sentiment(symbol):
    params = {'function': 'SOCIAL_SENTIMENT', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_earning_call_transcript(symbol):
    params = {'function': 'EARNING_CALL_TRANSCRIPT', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_dividends(symbol):
    params = {'function': 'DIVIDENDS', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_splits(symbol):
    params = {'function': 'SPLITS', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_historical_volatility(symbol):
    params = {'function': 'HISTORICAL_VOLATILITY', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_bankruptcy(symbol):
    params = {'function': 'BANKRUPTCY', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_delisting(symbol):
    params = {'function': 'DELISTING', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_sec_filings(symbol):
    params = {'function': 'SECFILINGS', 'symbol': symbol, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]


def stock_earnings_calendar_today():
    params = {'function': 'EARNINGS_CALENDAR', 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]


def stock_sma(symbol, interval='daily', time_period=30, series_type='close'):
    params = {'function': 'SMA', 'symbol': symbol, 'interval': interval, 'time_period': time_period, 'series_type': series_type, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_ema(symbol, interval='daily', time_period=30, series_type='close'):
    params = {'function': 'EMA', 'symbol': symbol, 'interval': interval, 'time_period': time_period, 'series_type': series_type, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_rsi(symbol, interval='daily', time_period=14, series_type='close'):
    params = {'function': 'RSI', 'symbol': symbol, 'interval': interval, 'time_period': time_period, 'series_type': series_type, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]

def stock_macd(symbol, interval='daily', series_type='close', fast_period=12, slow_period=26, signal_period=9):
    params = {'function': 'MACD', 'symbol': symbol, 'interval': interval, 'series_type': series_type, 'fast_period': fast_period, 'slow_period': slow_period, 'signal_period': signal_period, 'apikey': API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.text[:3000]


