"""
core/nlp.py
-----------

Natural Language Processing (NLP) engine for Karen.
"""

import string

from config import STOP_WORDS, INTENTS, ENTITIES


class NLPProcessor:
    """
    Processes user commands and converts them into
    structured data that Karen can understand.
    """

    def __init__(self):
        """
        Initialize the NLP processor.
        """
        pass

    # ==========================================================
    # Normalize Text
    # ==========================================================

    def normalize(self, text: str) -> str:
        """
        Normalize the user's input.

        Steps:
        - Convert to lowercase
        - Remove leading/trailing spaces
        - Remove punctuation
        """

        text = text.lower()
        text = text.strip()

        text = text.translate(
            str.maketrans(
                "",
                "",
                string.punctuation
            )
        )

        return text

    # ==========================================================
    # Tokenize Text
    # ==========================================================

    def tokenize(self, text: str) -> list[str]:
        """
        Splits a sentence into individual words.
        """

        return text.split()

    # ==========================================================
    # Remove Stop Words
    # ==========================================================

    def remove_stop_words(
        self,
        tokens: list[str]
    ) -> list[str]:
        """
        Removes unnecessary words from a list of tokens.

        Args:
            tokens (list[str]): Tokenized sentence.

        Returns:
            list[str]: Tokens after removing stop words.
        """

        filtered_tokens = []

        for word in tokens:

            if word not in STOP_WORDS:

                filtered_tokens.append(word)

        return filtered_tokens
    
    # ==========================================================
    # Detect Intent
    # ==========================================================

    def detect_intent(
        self,
        tokens: list[str]
    ) -> str | None:
        """
        Detect the user's intent from the token list.

        Args:
            tokens (list[str]): Filtered tokens.

        Returns:
            str | None: Detected intent or None.
        """

        for word in tokens:

            for intent, keywords in INTENTS.items():

                if word in keywords:

                    return intent

        return None
    
# ==========================================================
# Extract Entity
# ==========================================================

    def extract_entity(
        self,
        tokens: list[str]
    ) -> dict | None:
        """
        Extracts the entity from the token list.

        Args:
            tokens (list[str]): Filtered tokens.

        Returns:
            dict | None:
                {
                    "type": "...",
                    "entity": "..."
                }
        """

        for word in tokens:

            for entity_type, entities in ENTITIES.items():

                if word in entities:

                    return {

                        "type": entity_type,

                        "entity": word

                    }

        return None

# ==========================================================
# Process Command
# ==========================================================

    def process(
        self,
        text: str
    ) -> dict:
        """
        Runs the complete NLP pipeline.

        Args:
            text (str): User input.

        Returns:
            dict: Structured NLP result.
        """

        normalized = self.normalize(text)

        tokens = self.tokenize(normalized)

        filtered_tokens = self.remove_stop_words(tokens)

        intent = self.detect_intent(filtered_tokens)

        entity = self.extract_entity(filtered_tokens)

        return {

            "original": text,

            "normalized": normalized,

            "tokens": tokens,

            "filtered_tokens": filtered_tokens,

            "intent": intent,

            "entity": entity

        }
