"""
commands/jokes.py
-----------------

Handles telling jokes.
"""

import pyjokes

from commands.base import BaseCommand


class JokeCommand(BaseCommand):
    """
    Handles joke-related commands.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Tell Joke
    # ==========================================================

    def tell_joke(self) -> None:
        """
        Tells a random programming joke.
        """

        try:

            joke = pyjokes.get_joke()

            self.logger.info(
                "Told a joke."
            )

            self.speech.speak(joke)

        except Exception as error:

            self.logger.error(str(error))

            self.speech.speak(
                "Sorry, I couldn't think of a joke right now."
            )