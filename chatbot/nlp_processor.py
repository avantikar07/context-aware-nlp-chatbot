import nltk
import spacy

# Load the spaCy English language model
nlp = spacy.blank("en")


def tokenize_text(text):
    """
    Tokenize the user's input into individual words/tokens.
    """
    tokens = nltk.word_tokenize(text)
    return tokens


def process_text(text):
    """
    Process the user's input using spaCy.
    """
    doc = nlp(text)

    processed_tokens = []

    for token in doc:
        processed_tokens.append(token.text)

    return processed_tokens