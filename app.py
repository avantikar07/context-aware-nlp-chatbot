from flask import Flask, render_template, request

from chatbot.context_manager import ContextManager
from chatbot.intent_classifier import chatbot_response


app = Flask(__name__)

# Create a context manager for the conversation
context_manager = ContextManager()


@app.route("/")
def home():
    """
    Display the chatbot web page.
    """
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receive the user's message and return the chatbot response.
    """

    user_message = request.form["message"]

    response = chatbot_response(
        user_message,
        context_manager
    )

    return response


if __name__ == "__main__":
    app.run(debug=True)