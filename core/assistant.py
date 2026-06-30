"""
core/assistant.py
-----------------

Main assistant class for Karen.
"""

from core.speech import SpeechManager
from core.logger import Logger
from core.nlp import NLPProcessor
from core.registry import CommandRegistry
from core.assistant_utilities import AssistantUtilities

from commands.browser import BrowserCommand
from commands.music import MusicCommand
from commands.wikipedia import WikipediaCommand
from commands.screenshot import ScreenshotCommand
from commands.jokes import JokeCommand
from commands.system import SystemCommand
from commands.assistant_name import AssistantNameCommand


class KarenAssistant:
    """
    Main controller of Karen Voice Assistant.
    """

    def __init__(self):
        """
        Initialize all components of Karen.
        """

        # ======================================================
        # Core Components
        # ======================================================

        self.logger = Logger()

        self.speech = SpeechManager()

        self.nlp = NLPProcessor()

        self.utilities = AssistantUtilities(self)

        # ======================================================
        # Command Modules
        # ======================================================

        self.browser = BrowserCommand(self)

        self.music = MusicCommand(self)

        self.wikipedia = WikipediaCommand(self)

        self.screenshot = ScreenshotCommand(self)

        self.jokes = JokeCommand(self)

        self.system = SystemCommand(self)

        self.assistant_name = AssistantNameCommand(self)

        # ======================================================
        # Command Registry
        # ======================================================

        self.registry = CommandRegistry(self)

    # ==========================================================
    # Run Assistant
    # ==========================================================

    def run(self) -> None:
        """
        Starts Karen's main loop.
        """

        self.speech.speak(
            "Hello, I am Karen. How can I help you?"
        )

        while True:

            # Listen to the user
            query = self.speech.listen()

            if query is None:

                continue

            # Process the command
            result = self.nlp.process(query)

            intent = result["intent"]

            entity = result["entity"]

            # No intent detected
            if intent is None:

                self.speech.speak(
                    "Sorry, I couldn't understand your request."
                )

                continue

            # Execute the command
            success = self.registry.execute(

                intent,

                entity

            )

            if not success:

                self.logger.warning(
                    f"Failed to execute intent: {intent}"
                )