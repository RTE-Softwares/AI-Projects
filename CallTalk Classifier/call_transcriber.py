
from langchain_community.chat_models import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent,tool
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel,Field
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv.main import load_dotenv
import os
load_dotenv()

openai_api_key = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(api_key=openai_api_key,model="gpt-3.5-turbo-1106")

openai_client = OpenAI()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

class audio_explainer(BaseModel):
    path_to_audio:str=Field(description="This is the path of the recording")

  
@tool(args_schema=audio_explainer)
def audio_summarizer(path_to_audio:str): 
    "Useful for when you need to process audio file"
    audio_file= open(path_to_audio, "rb")
    transcript = openai_client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
            response_format="text",
            language="en"
        )
    prompt = ChatPromptTemplate.from_template(
    "based on this conversation between person1 and person2   make a chat {conversation}"
    )
    output_parser = StrOutputParser()
    model = ChatOpenAI(model="gpt-3.5-turbo")
    chain = (
        prompt
        | model
        | output_parser
    )
    for chunk in chain.stream({"conversation":transcript}):
        print(chunk, end="", flush=True)
    return transcript

prompt = hub.pull("hwchase17/openai-functions-agent")
tools = [audio_summarizer]
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,memory=memory)
while True:
    req=input("requirement ::  ")
    print(agent_executor.invoke({"input": req,"chat_history":memory.chat_memory.messages}))
