# speech code here:w
"""
core/speech.py

Handles all speech input and output.
"""

from typing import Optional

import pyttsx3
import speech_recognition as sr

from config import (
    VOICE_INDEX,
    VOICE_RATE,
    VOICE_VOLUME,
    LANGUAGE,
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT,
    AMBIENT_NOISE_DURATION,
)


class SpeechManager:
    """
    Handles speech recognition
    and text-to-speech.
    """

    def __init__(self):

        self.engine = pyttsx3.init()

        voices = self.engine.getProperty("voices")

        if len(voices) > VOICE_INDEX:
            self.engine.setProperty(
                "voice",
                voices[VOICE_INDEX].id
            )

        self.engine.setProperty(
            "rate",
            VOICE_RATE
        )

        self.engine.setProperty(
            "volume",
            VOICE_VOLUME
        )

        self.recognizer = sr.Recognizer()

    # -----------------------------------

    def speak(self, text: str) -> None:
        """
        Speak the given text.
        """

        print(f"\nKaren : {text}")

        self.engine.say(text)
        self.engine.runAndWait()

    # -----------------------------------

    def listen(self) -> Optional[str]:
        """
        Listen through the microphone
        and return recognized speech.
        """

        try:

            with sr.Microphone() as source:

                print("\nListening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=AMBIENT_NOISE_DURATION
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )

            print("Recognizing...")

            query = self.recognizer.recognize_google(
                audio,
                language=LANGUAGE
            )

            query = query.lower()

            print(f"\nYou : {query}")

            return query

        except sr.WaitTimeoutError:

            self.speak("I didn't hear anything.")

        except sr.UnknownValueError:

            self.speak("Sorry, I couldn't understand.")

        except sr.RequestError:

            self.speak(
                "Speech recognition service is unavailable."
            )

        except OSError:

            self.speak("Microphone not found.")

        except Exception as error:

            print(error)

            self.speak("Something went wrong.")

        return None