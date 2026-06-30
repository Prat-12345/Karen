"""
commands/screenshot.py
----------------------

Handles taking screenshots.
"""

from datetime import datetime

import pyautogui

from config import PICTURES_DIR, SCREENSHOT_PREFIX
from commands.base import BaseCommand


class ScreenshotCommand(BaseCommand):
    """
    Handles screenshot operations.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Take Screenshot
    # ==========================================================

    def take_screenshot(self) -> None:
        """
        Takes a screenshot and saves it.
        """

        try:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = (
                f"{SCREENSHOT_PREFIX}_{timestamp}.png"
            )

            filepath = PICTURES_DIR / filename

            screenshot = pyautogui.screenshot()

            screenshot.save(filepath)

            self.logger.info(
                f"Screenshot saved: {filepath}"
            )

            self.speech.speak(
                "Screenshot captured successfully."
            )

        except Exception as error:

            self.logger.error(str(error))

            self.speech.speak(
                "I couldn't take the screenshot."
            )