
from langchain_community.chat_models import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent,tool
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel,Field
from openai import OpenAI
import pytube as pt
from dotenv.main import load_dotenv
import os
load_dotenv()

openai_api_key = os.environ['API_KEY']

llm = ChatOpenAI(api_key=openai_api_key,model="gpt-3.5-turbo-1106")

openai_client = OpenAI(api_key=openai_api_key)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

class youtube_link(BaseModel):
    path_to_audio:str=Field(description="This is the link")

  
@tool(args_schema=youtube_link)
def youtube_transcriber(path_to_audio:str): 
    "Useful for when you need to process links to transcribe them"
    yt = pt.YouTube(path_to_audio)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename="audio_english.mp3")   
    audio_file= open("audio_english.mp3", "rb")
    transcript = openai_client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
            response_format="text",
            language="en"
        )
    return transcript

prompt = hub.pull("hwchase17/openai-functions-agent")
tools = [youtube_transcriber]
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,memory=memory)
while True:
    req=input("requirement ::  ")
    print(agent_executor.invoke({"input": req,"chat_history":memory.chat_memory.messages}))