import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List
from langchain.agents import initialize_agent
from langchain import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from agents import tools

os.environ['OPENAI_API_KEY'] = "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"
models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Set up the turbo LLM
llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-3.5-turbo'
)

@textbase.chatbot("talking-bot")
def on_message(message_history: dict, state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """
    print(message_history)
    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    """
        bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )
    print(bot_response)
    """

    # conversational agent memory
    memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )


    # create our agent
    bot = initialize_agent(
        agent='chat-conversational-react-description',
        tools=tools,
        llm=llm,
        verbose=True,
        max_iterations=3,
        early_stopping_method='generate',
        memory=memory
    )

    fixed_prompt = """
    Financial Analysts play a crucial role in the world of finance, utilizing their expertise to analyze and interpret complex financial data. They are skilled professionals who assess the financial health and performance of companies, make investment recommendations, and provide strategic insights to aid in decision-making processes.

    A financial analyst's key responsibilities include conducting thorough research, evaluating financial statements, and assessing market trends to identify potential investment opportunities or risks. They use various quantitative and qualitative methods to develop financial models and projections, helping businesses and investors make informed choices.

    Additionally, financial analysts monitor economic conditions, industry developments, and regulatory changes that could impact financial markets. They collaborate with teams to prepare comprehensive reports and presentations, communicating their findings effectively to stakeholders.

    Continuous learning is essential for financial analysts as they need to stay updated with the latest market trends, tools, and methodologies. Their analytical skills, attention to detail, and ability to think critically are indispensable assets in the dynamic world of finance.

    In summary, financial analysts are vital players in the financial landscape, providing valuable insights and guidance to optimize financial performance and achieve business objectives. Their expertise contributes significantly to informed decision-making and successful financial strategies.
    """
    bot.agent.llm_chain.prompt.messages[0].prompt.template = fixed_prompt
    message_history = [message_history[-1]]
    bot_response = bot(message_history[0].content)
    return bot_response['output'], state
