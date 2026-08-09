from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Memory
conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Keep replies short and friendly."
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data["message"]
    
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=conversation_history
    )
    
    reply = response.choices[0].message.content
    
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    return jsonify({"response": reply})
#this is for live deployment on railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)