# Financial Analyst AI - Co-Pilot

## Introduction

Welcome to Co-Pilot, your intelligent financial analyst AI. Co-Pilot is designed to provide you with real-time access to data in the stock market, the latest news, and a plethora of tools to assist you in making informed financial decisions. With Co-Pilot, you can save time and effort by bypassing the need to sift through countless articles and conduct extensive research on your own. Let's take a look at some of the key features of Co-Pilot.

## Real-Time News Access

Co-Pilot keeps you updated with the latest news related to the financial world. It scans the internet and aggregates the hot topics, such as concerns over Federal Reserve rates, market cycles, and positive GDP growth. With Co-Pilot, you can stay ahead of the curve and make decisions based on up-to-date information.

## Stock Price Tracker

Stay on top of stock prices with Co-Pilot's real-time stock price tracker. Whether you need to know the current price of a specific stock or a whole portfolio, Co-Pilot can fetch the latest data for you. For instance, if you want to check the current price of Tesla stock, simply ask Co-Pilot, and it will provide you with the most recent value.

## Fundamental Data Access

Dig deep into the fundamentals of stocks with Co-Pilot's comprehensive access to financial data. Whether it's Tesla's quarterly capitalization, PE ratio, 52-week high, or cash flow statements, Co-Pilot has got you covered. You can easily retrieve essential information about any company, saving you time and effort.

## YouTube Video and Website Analysis

Co-Pilot goes beyond text-based data and can analyze YouTube videos and websites for you. If you have a specific video discussing market trends or a website with crucial financial information, Co-Pilot can process the content and summarize it for you. This feature ensures you have access to diverse sources of information to support your decisions.

## Alpha Advantage API Integration

Co-Pilot harnesses the power of the Alpha Advantage API, providing you with a wide range of financial tools and information. You can access time series data, stock overviews, earnings reports, technical indicators, and much more. The Alpha Advantage integration enhances Co-Pilot's capabilities, making it a comprehensive financial assistant.

## Wikipedia Integration

In case Co-Pilot encounters unfamiliar terms or topics outside its knowledge base, it can quickly refer to Wikipedia to fetch the necessary information. This ensures that you receive accurate and detailed answers to your queries.

## Future Enhancements

Co-Pilot is just the beginning. It can be further enhanced by integrating other APIs and services, such as Elastic Search, to expand its data sources and provide even more valuable insights.

In summary, Co-Pilot is your ultimate financial analyst AI, offering real-time access to stock market data, news, and a plethora of tools to support your financial decisions. It's designed to be your co-pilot, assisting you on your financial journey, saving you time, and empowering you with accurate and timely information. The possibilities are endless, and Co-Pilot is ready to take flight with you.

---
Please note that the above README file is a brief summary of the features and capabilities of your Financial Analyst AI - Co-Pilot. You can expand on this and provide more details and documentation based on your specific implementation and any future enhancements you plan to make.

# Textbase

✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py` and Textbase will take care of the rest :)

Since it is just Python you can use whatever models, libraries, vector databases and APIs you want.

_Coming soon:_

- [ ] PyPI package
- [ ] SMS integration
- [ ] Easy web deployment via `textbase deploy`
- [ ] Native integration of other models (Claude, Llama, ...)

## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/JaydenCS/Financial_Co_Pilot
cd Financial_Co_Pilot	
poetry install
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:

```bash
poetry run python textbase/textbase_cli.py test main.py
```

Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your bot! The bot will automatically reload when you change the code.

_Simpler version using PyPI package and CLI coming soon!_
## Other Requirements 

- In order to work with full functionality please install requirements.txt on poetry by running the following command

```bash
poetry run pip install -r requirements.txt
```
