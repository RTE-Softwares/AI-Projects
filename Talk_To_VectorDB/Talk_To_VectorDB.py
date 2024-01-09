

from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent,tool
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel,Field
from openai import OpenAI
from dotenv.main import load_dotenv
import chromadb
import os

client = chromadb.PersistentClient(path="./")
load_dotenv()

openai_key = os.environ['API_KEY']
llm = ChatOpenAI(api_key=openai_key,model="gpt-3.5-turbo-1106")
openai_client = OpenAI()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


class database_answers(BaseModel):
    user_query_text:str=Field(description="This is the full query")
@tool(args_schema=database_answers)
def vector_db(user_query_text): 
    "use this when user ask any type of question related "
    collection = client.get_or_create_collection(name="test")
    collection.add(
    documents=["harrison was a brave boy","harrison was a boy with black hairs"],
    ids=["id1","id2"]
    )
    print(collection.get())
    results = collection.query(
    query_texts=[user_query_text],
    n_results=2
    )["documents"][0]

    prompt = ChatPromptTemplate.from_template( """Answer the question based only on the following context:

    {results}

    Question: {user_query_text}
    
    """)
    chain = prompt|llm| StrOutputParser()
    chain=chain.invoke({"results": results,"user_query_text":user_query_text})
    print(chain)
    return chain

class no_response(BaseModel):
    user_query_text:str=Field(description="This is the full query")
@tool(args_schema=no_response)
def validation_tool(user_query_text): 
    "only use this tool whenever vector_db tool have no answer "
    collection = client.get_or_create_collection(name="test")
    data=collection.get()["documents"][0]
    prompt = ChatPromptTemplate.from_template("""user asked us this question but we have this data explain him what info we have related to user's question 
    data :
    {data}

    Question: {user_query_text}

        """)
    
    chain = prompt| llm| StrOutputParser()
    chain=chain.invoke({"data": data,"user_query_text":user_query_text})
    
    return chain

prompt = hub.pull("hwchase17/openai-functions-agent")
tools = [vector_db,validation_tool]
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,memory=memory)
while True:
    req=input("requirement ::  ")
    print(agent_executor.invoke({"input": req,"chat_history":memory.chat_memory.messages}))

