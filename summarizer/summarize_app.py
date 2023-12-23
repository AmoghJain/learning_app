from summarizer import summarizer
from flask import Flask, request, jsonify

app = Flask(__name__)
summarize_obj = summarizer()

@app.route("/", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data["text"]
    result = summarize_obj.run(text)
    return result