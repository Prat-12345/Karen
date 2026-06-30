"""
commands/assistant_name.py
--------------------------

Manages Karen's name.
"""

from config import ASSISTANT_NAME, ASSISTANT_NAME_FILE
from commands.base import BaseCommand


class AssistantNameCommand(BaseCommand):
    """
    Handles loading, saving, and changing Karen's name.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Load Karen's Name
    # ==========================================================

    def load_name(self) -> str:
        """
        Returns Karen's current name.
        """

        try:

            if ASSISTANT_NAME_FILE.exists():

                name = ASSISTANT_NAME_FILE.read_text().strip()

                if name:
                    return name

        except Exception as error:

            print(f"Error loading assistant name: {error}")

        return ASSISTANT_NAME

    # ==========================================================
    # Save Karen's Name
    # ==========================================================

    def save_name(self, name: str) -> None:
        """
        Saves Karen's name.
        """

        try:

            ASSISTANT_NAME_FILE.write_text(name)

        except Exception as error:

            print(f"Error saving assistant name: {error}")

            self.speech.speak(
                "Sorry, I couldn't save my name."
            )

    # ==========================================================
    # Change Karen's Name
    # ==========================================================

    def change_name(self) -> None:
        """
        Changes Karen's name using voice input.
        """

        self.speech.speak(
            "What would you like to call me?"
        )

        new_name = self.speech.listen()

        if not new_name:

            self.speech.speak(
                "I couldn't understand the new name."
            )

            return

        new_name = new_name.title().strip()

        self.save_name(new_name)

        self.speech.speak(
            f"My new name is {new_name}."
        )