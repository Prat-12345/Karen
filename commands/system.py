"""
commands/system.py
------------------

Handles system-related commands.
"""

import os

from commands.base import BaseCommand


class SystemCommand(BaseCommand):
    """
    Handles system operations.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Shutdown Computer
    # ==========================================================

    def shutdown(self) -> None:
        """
        Shuts down the computer.
        """

        self.logger.info(
            "Shutdown requested."
        )

        self.speech.speak(
            "Shutting down the computer."
        )

        os.system("shutdown /s /f /t 1")

    # ==========================================================
    # Restart Computer
    # ==========================================================

    def restart(self) -> None:
        """
        Restarts the computer.
        """

        self.logger.info(
            "Restart requested."
        )

        self.speech.speak(
            "Restarting the computer."
        )

        os.system("shutdown /r /f /t 1")

    # ==========================================================
    # Exit Karen
    # ==========================================================

    def exit(self) -> bool:
        """
        Stops Karen.

        Returns:
            bool: False indicates the assistant should stop.
        """

        self.logger.info(
            "Karen is shutting down."
        )

        self.speech.speak(
            "Goodbye! Have a nice day."
        )

        return False