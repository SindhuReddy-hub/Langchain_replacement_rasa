from fastapi import FastAPI, Request
from pydantic import BaseModel
from chatbot import run_chatbot

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(user_msg: UserMessage):
    response = run_chatbot(user_msg.message)
    return {"response": response}
