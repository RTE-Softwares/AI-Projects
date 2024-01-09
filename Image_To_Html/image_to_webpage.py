
from langchain_community.chat_models import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent,tool
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel,Field
import base64
from openai import OpenAI
from dotenv.main import load_dotenv
import os
load_dotenv()

openai_api_key = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(api_key=openai_api_key,model="gpt-3.5-turbo-1106")

openai_client = OpenAI()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

class Image_Explainer(BaseModel):
    path_of_image:str=Field(description="This is the path of image from the string")
    user_requirement:str=Field(description="full requirement related to image")

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
@tool(args_schema=Image_Explainer)
def image_processor(path_of_image:str,user_requirement:str): 
    "Useful for when you need explain something about image"
    base64_image = encode_image(path_of_image)
    response = openai_client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
    {
        "role": "user",
        "content": [
        {"type": "text", "text": user_requirement},
        {
            "type": "image_url",
            "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
            },
        },
        ],
    }
    ],
    max_tokens=2000,
    ).choices[0].message.content
    return response

prompt = hub.pull("hwchase17/openai-functions-agent")
tools = [image_processor]
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,memory=memory)
while True:
    req=input("requirement ::  ")
    print(agent_executor.invoke({"input": req,"chat_history":memory.chat_memory.messages}))
