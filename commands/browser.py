"""
commands/browser.py
-------------------

Handles opening websites in the default browser.
"""

import webbrowser

from config import WEBSITES
from commands.base import BaseCommand


class BrowserCommand(BaseCommand):
    """
    Handles browser-related commands.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Open Website
    # ==========================================================

    def open_website(self, website: str) -> None:
        """
        Opens a website using its alias.

        Args:
            website (str): Name or alias of the website.
        """

        website = website.lower().strip()

        url = WEBSITES.get(website)

        if url is None:

            self.logger.warning(
                f"Unknown website requested: {website}"
            )

            self.speech.speak(
                f"Sorry, I don't know how to open {website}."
            )

            return

        self.logger.info(
            f"Opening website: {website}"
        )

        self.speech.speak(
            f"Opening {website}."
        )

        webbrowser.open(url)