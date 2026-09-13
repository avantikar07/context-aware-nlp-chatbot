import json
import random

from chatbot.nlp_processor import tokenize_text


with open("data/intents.json", "r") as file:
    intents_data = json.load(file)
def get_intent(user_input):
    """
    Find the intent that best matches the user's input.
    """

    user_tokens = set(tokenize_text(user_input.lower()))

    best_intent = None
    best_score = 0

    for intent in intents_data["intents"]:
        for pattern in intent["patterns"]:

            pattern_tokens = set(tokenize_text(pattern.lower()))

            common_words = user_tokens.intersection(pattern_tokens)

            score = len(common_words)

            if score > best_score:
                best_score = score
                best_intent = intent["tag"]

    return best_intent
def get_response(intent_tag):
    """
    Generate a response based on the detected intent.
    """

    for intent in intents_data["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])

    return "Sorry, I don't understand your question."
def chatbot_response(user_input, context_manager):
    """
    Process user input and use conversation context
    to generate a response.
    """

    intent = get_intent(user_input)

    # If an intent is detected, update the context
    if intent is not None:
        context_manager.update_context(intent)

        return get_response(intent)

    # If no new intent is detected, check previous context
    previous_intent = context_manager.get_context()

    if previous_intent == "working_hours":
        return "The college is closed on Sunday."

    return "Sorry, I don't understand your question."