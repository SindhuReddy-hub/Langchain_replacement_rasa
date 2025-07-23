import redis
from langchain.memory import ConversationBufferMemory

class RedisMemory(ConversationBufferMemory):
    def __init__(self, session_id: str):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        self.session_id = session_id
        super().__init__(memory_key="chat_history", return_messages=True)

    def save_context(self, inputs, outputs):
        history_key = f"chat:{self.session_id}"
        conversation = self.redis_client.get(history_key) or b""
        new_entry = f"User: {inputs}\nBot: {outputs}\n"
        updated_conversation = conversation.decode() + new_entry
        self.redis_client.set(history_key, updated_conversation)
        self.chat_memory.add_user_message(inputs)
        self.chat_memory.add_ai_message(outputs)

    def load_memory_variables(self, inputs):
        return {"chat_history": self.redis_client.get(f"chat:{self.session_id}").decode()}
