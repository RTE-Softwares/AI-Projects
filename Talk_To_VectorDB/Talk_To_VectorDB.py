
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import tool
from langchain_community.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_openai_functions_agent,tool
from pydantic import BaseModel,Field

from langchain.agents import initialize_agent
from openai import OpenAI

from dotenv.main import load_dotenv

import chromadb
from langchain import hub
import os

from langchain.agents import initialize_agent

client = chromadb.PersistentClient(path="./")

load_dotenv()

openai_key = os.environ['API_KEY']
llm = ChatOpenAI(api_key=openai_key,model="gpt-4-1106-preview")
openai_client = OpenAI(api_key=openai_key)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


class database_answers(BaseModel):
    paragraph:str=Field(description="This is the question asked by user ")
    user_query:str=Field(description="This is the  latest question asked by user")
@tool(args_schema=database_answers)
def question_asker(paragraph=None,user_query=None): 
    "use this tool when any question is asked"

    print("user_query_text >>>>>>>>>>>",paragraph)
    print('latest_user_query >>>>>>>>>>>>',user_query)
    collection = client.get_or_create_collection(name="test3")
    # collection.add(
    #     documents=["sheep","peacock","hen","bull","dog","Horse","Cat","Snake","rabbit","Parrot","Cow","Fish","Duck","Goat"],
    #     ids=["id1","id2","id3","id4","id5","id6","id7","id8","id9","id10","id11","id12","id13","id14"]
    # )
    #print(collection.get())

    results = collection.query(
        query_texts=[user_query + paragraph],
        n_results=1
    )["documents"][0]
 
    prompt = ChatPromptTemplate.from_template("""Is this could be the correct answer based on question and description 

    question: {initial_user_query} 
                                              
    description : {paragraph}
                                                

    answer: {result}
                                              
    'if answer is correct then say the final answer is 'answer' '
    'otherwise say incorrect answer   

    donot give additional information in your response it should always be from the above two                                    
    """)
    chain = prompt| llm| StrOutputParser()
    response=chain.invoke({"initial_user_query":user_query,"paragraph":paragraph,'result':results})
    
    print("animal results ::", results)

    print("response from gpt  ::",response)
    return response

# which bird is most eaten by humans

@tool
def user_query_maker(user_query_text): 
    "only use this tool to make paragraph and also when question_asker have incorrect answer "

    prompt = ChatPromptTemplate.from_template("""give the paragraph solution for this 
 
    query: {user_query_text} 
    """)
    
    chain = prompt| llm| StrOutputParser()
    latest_query=chain.invoke({"user_query_text":user_query_text})
    print(latest_query)
    return "Now The new paragraph value is " + latest_query 

tools = [question_asker,user_query_maker]

prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt)
# Assuming prompt.messages is a list of message objects
for message in prompt.messages:
    # Check if the message object has an attribute 'prompt' that in turn has an attribute 'template'
    if hasattr(message, 'prompt') and hasattr(message.prompt, 'template'):
        if message.prompt.template=='You are a helpful assistant':
            message.prompt.template="You are helpful assistant and always rely on tools for the answer donot use your own knowledge and when you find paragraph value from user_query_maker tool use it in the  question_asker tool to get suitable answer if this tool gives wrong answer do the same iteration and if we dnot get the write answer in the final answer say 'we donot have any record for this in our database"

print(prompt)
agent = create_openai_functions_agent(llm, tools,prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# print(agent_executor.agent.llm_chain.prompt.template)
# print(agent_executor.agent.llm_chain.prompt.template)


while True:
    req=input("requirement ::  ")
    print(agent_executor.invoke({"input": req}))

