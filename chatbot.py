from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools.aws_tools import list_s3_buckets

tools = [
    Tool(name="List S3 Buckets", func=list_s3_buckets, description="Lists all AWS S3 buckets")
]

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(tools, llm, agent="chat-conversational-react-description", memory=memory, verbose=True)

def run_chatbot(input_text):
    return agent.run(input_text)
