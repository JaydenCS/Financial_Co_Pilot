from langchain.agents import Tool
from alphatools import *
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import OpenAI
from webscraper import get_all_text_content
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
from youtube import get_transcript
def human(query):
    human_llm = OpenAI(temperature=0.0)
    response = human_llm(prompt=f"Based on the input given find what is the additional data that needs to be known to solve this and ask to the user in the most poliet manner, Input:{query}")
    return response
search_duck = DuckDuckGoSearchRun()
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

tools = [
    Tool(
        name = "Time series daily",
        func=time_series_daily,
        description="useful for when you need to answer questions regarding daily time series data of stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Time series weekly",
        func=time_series_intraday,
        description="useful for when you need to answer questions regarding weekly time series data of stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Time series monthly",
        func=time_series_monthly,
        description="useful for when you need to answer questions regarding montly time series data of stock or based on that this data, pass in the stock ticker as input"
    ),
    Tool(
        name = "Quote",
        func=quote_endpoint,
        description="useful for when you need to answer questions regarding quote data, pass in the stock ticker as input"
    ),
    Tool(
        name = "Search stock ticker",
        func=search_endpoint,
        description="useful for when you need to get the specific stock ticker, pass in the keyword as input"
    ),
    Tool(
        name = "Adjusted Volume",
        func=stock_time_series_adjusted_volume,
        description="useful for when you need to answer questions regarding volume of stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock Overview",
        func=stock_company_overview,
        description="useful for when you need to get idea about a company or a give an overview, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock Earning",
        func=stock_earnings,
        description="useful for when you need to get idea about the earnings of a company, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock income",
        func=stock_income_statement,
        description="useful for when you need to analyze the income of a company or get the income statement, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock Balance sheet",
        func=stock_balance_sheet,
        description="useful for when you need to get the balance sheet of a company for answering or analyzing, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock cash flow",
        func=stock_cash_flow,
        description="useful for when you need to get the cash flow statement of a company, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock latest news",
        func=stock_latest_news,
        description="useful for when you need to get the current news of a company or to know whats happening around them, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock news sentiment",
        func=stock_news_sentiment,
        description="useful for when you need to understand or get the sentiments of a company regarding a news, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock social sentiment",
        func=stock_social_sentiment,
        description="useful for when you need to understand the current social sentiment of the comapany or a stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock earnining call",
        func=stock_earning_call_transcript,
        description="useful for when you need to get the stock earning call of a company, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock splits",
        func=stock_dividends,
        description="useful for when you need to get the stock split of a company, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock sec filling",
        func=stock_sec_filings,
        description="useful for when you need to get the sec filing or report of a company, pass in the stock ticker as input"
    )
    ,
    Tool(
        name = "Stock sma",
        func=stock_sma,
        description="useful for when you need to calculate simple standard moving average of a stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock ema",
        func=stock_ema,
        description="useful for when you need to calculate exponetial moving average of a stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock macd",
        func=stock_macd,
        description="useful for when you need to calculate the macd of a stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Stock rsi",
        func=stock_rsi,
        description="useful for when you need to calculate the rsi of a stock, pass in the stock ticker as input"
    ),
    Tool(
        name = "Web Search",
        func=search_duck.run,
        description="useful for when you do web search regarding general topics or acquire general data"
    ),
    Tool(
        name = "Human",
        func=human,
        description="useful for when you need more data requirement or more knowledge to solve a question. This is the ultimate knowledge source that can help you get the answer. Pass in the query"
    ),Tool(
        name = "Youtube Scrapper",
        func=get_transcript,
        description="useful for when you need to get transcript from a youtube url to do the answering. Pass in the youtube url"
    ),
    Tool(
        name = "Web scrapper",
        func=get_all_text_content,
        description="useful for when you need to get the data from a url to do the answering. Pass in the url"
    ),
    Tool(
        name = "Wikipedia",
        func=wikipedia.run,
        description="useful for when you need the help of a encylopedia, this will give you access to wikipedia the online encylopedia. Pass in the keyword to search for"
    ),
    
]