# AI Chatbot 🤖

A full-stack AI chatbot web application built with Python and Flask.

## Features
- 💬 Real-time AI responses
- 🧠 Conversation memory
- 🎨 Beautiful chat interface
- ⚡ Fast responses via OpenRouter API
  
## 🌐 Live Demo
[Click here to chat!](https://ai-chatbot-flask-production-dfbb.up.railway.app/)

## Tech Stack
- Python
- Flask
- OpenRouter API (LLM)
- HTML/CSS/JavaScript
- python-dotenv

## How to run locally
1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt
3. Create .env file:
   OPENROUTER_API_KEY=your-key-here
4. Run:
   python chatbot.py
5. Open browser:
   http://localhost:5000

## Project Structure
project/
├── chatbot.py        # Flask backend
├── requirements.txt  # Dependencies
└── templates/
    └── index.html    # Chat interface
