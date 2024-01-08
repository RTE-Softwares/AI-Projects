# Import things that are needed generically
from langchain.agents import initialize_agent, tool
from langchain.tools import BaseTool
from langchain_community.chat_models import ChatOpenAI
import openai, pymysql
from langchain.prompts  import PromptTemplate
from langchain.chains import LLMChain
import  os
import json
os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = "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"

llm = ChatOpenAI(api_key="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",model="gpt-4")

class MysqlQueryBuilderTool(BaseTool):
    name = "MysqlQueryBuilder"
    description = "useful for when you need to create sql query from natural language"

    def _run(self, query: str) -> str:
        """Use the tool."""
        prompt = PromptTemplate(
            input_variables=["query"],
            template="""Assistant is a large language model trained by OpenAI.

                        Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

                        Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

                        Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

                        I want you to act as a sql query creator. I will type query in natural English language and you will reply with a real sql query with max 10 records limit. I want you to only reply with the sql query as output, and nothing else.
                        i have following tables in my database
                        1. customer (`CUST_CODE` (PRIMARY KEY),`CUST_NAME`,`CUST_CITY`,`WORKING_AREA`,`CUST_COUNTRY`,`GRADE`,`OPENING_AMT`,`RECEIVE_AMT`,`PAYMENT_AMT`,`OUTSTANDING_AMT`,`PHONE_NO`,`AGENT_CODE`(FORIEGN KEY))
                        2. orders (`ORD_NUM`(PRIMARY KEY),`ORD_AMOUNT`,`ADVANCE_AMOUNT`,`ORD_DATE`,`CUST_CODE`(FORIEGN KEY),`AGENT_CODE`(FORIEGN KEY),`ORD_DESCRIPTION`)
                        3. agents (`AGENT_CODE` (PRIMARY KEY),`AGENT_NAME`,`WORKING_AREA`,`COMMISSION`,`PHONE_NO`,`COUNTRY`)

                        If table name does not exists in query according to above available tables then final answer will be "Table doesn't exists" and quit the execution.
                        Human: {query}
                        Assistant:""",
        )

        chain = LLMChain(llm=llm, prompt=prompt)

        # Run the chain only specifying the input variable.
        return chain.run(query)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")

class FetchMysqlDataTool(BaseTool):
    name = "FetchMysqlData"
    description = "useful for when you need to fetch mysql data from a sql query"

    #create a function for db connection of mysql with params
    def db_connection(self):
        conn = None
        try:
            conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='emp')
        except Exception as e:
            print(e)
        return conn

    def _run(self, query: str) -> str:
        """Use the tool."""
        try:
            print("Find in db goes here.")
            conn2 = self.db_connection()
            cursor2 = conn2.cursor()
            print("query: ", query)
            cursor2.execute(query)
            response = cursor2.fetchall()
            print("response: ", response)
        except Exception as e:
            print("Table Exception :::", e)
            return None

        return response

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")

def db_bot(message: str):
    tools = [MysqlQueryBuilderTool(), FetchMysqlDataTool()]
    # agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    agent = initialize_agent(tools, llm, agent_path="langchain_2/agent.json", verbose=True)
    response = agent.run(message)
    is_valid_json = is_json(response)
    return {"response": response, "is_valid_json":is_valid_json}

# description create a function for check valid json format or not
# params json as input and
# returns output as boolean
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

db_bot("top buyers by sale")