"""
commands/base.py
----------------
Base class for all Karen commands.
"""


class BaseCommand:

    def __init__(self, assistant):

        self.assistant = assistant

    @property
    def speech(self):
        return self.assistant.speech

    @property
    def logger(self):
        return self.assistant.logger