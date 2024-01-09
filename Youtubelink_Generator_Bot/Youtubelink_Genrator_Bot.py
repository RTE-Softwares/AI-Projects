
from langchain_community.chat_models import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent,tool
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel,Field
from langchain.tools.youtube.search import YouTubeSearchTool
from openai import OpenAI
from dotenv.main import load_dotenv
import os
load_dotenv()

openai_api_key = os.environ['API_KEY']

llm = ChatOpenAI(api_key=openai_api_key,model="gpt-3.5-turbo-1106")

openai_client = OpenAI()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

class youtube_search(BaseModel):
    user_query_text:str=Field(description="this is title of the topic based on which user require link")


@tool(args_schema=youtube_search)
def youtube_search_tool(user_query_text): 
    "Useful for when you need to generate video or links Input should be the subject. "
    links=YouTubeSearchTool().run(user_query_text+",5")
    return links


prompt = hub.pull("hwchase17/openai-functions-agent")
tools = [youtube_search_tool]
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,memory=memory)
while True:
    req=input("requirement ::  ")
    print(agent_executor.invoke({"input": req,"chat_history":memory.chat_memory.messages}))