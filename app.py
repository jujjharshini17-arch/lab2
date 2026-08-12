from flask import Flask, request, jsonify
from google import genai
import os


app = Flask(__name__)


client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


@app.route("/")
def home():
    return "LLM API Running"


@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    prompt = data["prompt"]


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )


    return jsonify({
        "response": response.text
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)