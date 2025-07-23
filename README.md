# LangChain Chatbot Template (Rasa Alternative)

## Features
- Python 3.12 Compatible
- LangChain-based multi-turn chatbot
- Custom tools (e.g., AWS S3 CLI)
- FastAPI backend for easy integration

## Structure
- `chatbot.py` — Main conversation agent
- `tools/aws_tools.py` — Custom tools (add more as needed)
- `server/api.py` — FastAPI server for chatbot API

## Run the API
```bash
uvicorn server.api:app --reload
```

## Example Query
```bash
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"message": "List my s3 buckets"}'
```


Run the Streamlit Chatbot
Make sure your chatbot.py logic is working, then run:

bash
Copy
Edit
streamlit run ui/streamlit_chat.py

