class ContextManager:
    """
    Manage the conversation context of the chatbot.
    """

    def __init__(self):
        self.current_intent = None

    def update_context(self, intent):
        """
        Store the current conversation intent.
        """
        self.current_intent = intent

    def get_context(self):
        """
        Return the current conversation intent.
        """
        return self.current_intent

    def clear_context(self):
        """
        Clear the current conversation context.
        """
        self.current_intent = None