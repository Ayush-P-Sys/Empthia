from typing import Self
from flask import Flask, render_template, request
import ollama


app = Flask(__name__ , template_folder = 'template/')




@app.route("/")
def index():
    return render_template("Main.html")


@app.route("/ask")
def ask_page():
    return render_template("ask.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.data.decode("utf-8")  # Get user message from frontend
    response = ollama.chat(model="caspian:latest", messages=[{"role": "user", "content": user_input}])
    return response["message"]["content"]  # Send back the AI response



if __name__ == "__main__":
  app.run(debug = True)
