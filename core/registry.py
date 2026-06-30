"""
core/registry.py
----------------

Command registry for Karen.
"""


class CommandRegistry:
    """
    Registers and executes commands based on
    the intent detected by the NLP engine.
    """

    def __init__(self, assistant):
        """
        Initialize the command registry.
        """

        self.assistant = assistant

        self.commands = {

            # ==========================================
            # Browser
            # ==========================================

            "open_website": self.assistant.browser.open_website,

            # ==========================================
            # Music
            # ==========================================

            "play_music": self.assistant.music.play_music,

            # ==========================================
            # Wikipedia
            # ==========================================

            "wikipedia_search": self.assistant.wikipedia.search,

            # ==========================================
            # Utilities
            # ==========================================

            "tell_time": self.assistant.utilities.tell_time,

            "tell_date": self.assistant.utilities.tell_date,

            # ==========================================
            # Screenshot
            # ==========================================

            "take_screenshot": self.assistant.screenshot.take_screenshot,

            # ==========================================
            # Joke
            # ==========================================

            "tell_joke": self.assistant.jokes.tell_joke,

            # ==========================================
            # System
            # ==========================================

            "shutdown": self.assistant.system.shutdown,

            "restart": self.assistant.system.restart,

            "exit": self.assistant.system.exit,
        }


    # ==========================================================
    # Execute Command
    # ==========================================================

    def execute(
        self,
        intent: str,
        entity: dict | None = None
    ) -> bool:
        """
        Executes the command associated with the intent.
        """

        action = self.commands.get(intent)

        if action is None:

            self.assistant.speech.speak(
                "Sorry, I don't understand that command."
            )

            return False

        try:

            if entity and "entity" in entity:

                action(entity["entity"])

            else:

                action()

            return True

        except Exception as error:

            self.assistant.logger.error(
                f"Command execution failed: {error}"
            )

            self.assistant.speech.speak(
                "Sorry, something went wrong while executing the command."
            )

            return False

        