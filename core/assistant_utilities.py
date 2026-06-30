"""
core/assistant_utilities.py
---------------------------

Utility functions used by Karen.
"""

from datetime import datetime


class AssistantUtilities:
    """
    Provides utility functions for Karen.
    """

    def __init__(self, assistant):
        """
        Initialize the utility manager.

        Args:
            assistant: KarenAssistant instance.
        """
        self.assistant = assistant

    # ==========================================================
    # Wish User
    # ==========================================================

    def wish_user(self) -> None:
        """
        Greets the user according to the current time.
        """

        hour = datetime.now().hour

        assistant_name = self.assistant.name_command.load_name()

        if 5 <= hour < 12:
            greeting = "Good Morning"

        elif 12 <= hour < 17:
            greeting = "Good Afternoon"

        elif 17 <= hour < 21:
            greeting = "Good Evening"

        else:
            greeting = "Good Night"

        self.assistant.speech.speak(greeting)
        self.assistant.speech.speak(f"I am {assistant_name}.")
        self.assistant.speech.speak("How can I help you today?")

    # ==========================================================
    # Current Time
    # ==========================================================

    def get_current_time(self) -> str:
        """
        Returns the current time as a string.
        """

        return datetime.now().strftime("%I:%M:%S %p")

    def tell_time(self) -> None:
        """
        Speaks the current time.
        """

        current_time = self.get_current_time()

        self.assistant.speech.speak(
            f"The current time is {current_time}."
        )

    # ==========================================================
    # Current Date
    # ==========================================================

    def get_current_date(self) -> str:
        """
        Returns today's date as a string.
        """

        return datetime.now().strftime("%d %B %Y")

    def tell_date(self) -> None:
        """
        Speaks today's date.
        """

        current_date = self.get_current_date()

        self.assistant.speech.speak(
            f"Today's date is {current_date}."
        )