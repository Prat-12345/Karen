"""
commands/wikipedia.py
---------------------

Handles Wikipedia searches.
"""

import wikipedia

from commands.base import BaseCommand


class WikipediaCommand(BaseCommand):
    """
    Handles Wikipedia searches.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Search Wikipedia
    # ==========================================================

    def search(self, query: str) -> None:
        """
        Searches Wikipedia and reads a summary.

        Args:
            query (str): Search query.
        """

        query = query.strip()

        if not query:

            self.speech.speak(
                "Please tell me what you want to search."
            )

            return

        self.logger.info(
            f"Wikipedia Search: {query}"
        )

        self.speech.speak(
            f"Searching Wikipedia for {query}."
        )

        try:

            result = wikipedia.summary(
                query,
                sentences=2,
                auto_suggest=False
            )

            self.speech.speak(result)

        except wikipedia.exceptions.DisambiguationError:

            self.logger.warning(
                f"Multiple Wikipedia results for {query}"
            )

            self.speech.speak(
                "There are multiple results. Please be more specific."
            )

        except wikipedia.exceptions.PageError:

            self.logger.warning(
                f"Wikipedia page not found: {query}"
            )

            self.speech.speak(
                "I couldn't find anything on Wikipedia."
            )

        except Exception as error:

            self.logger.error(str(error))

            self.speech.speak(
                "Something went wrong while searching Wikipedia."
            )