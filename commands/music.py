"""
commands/music.py
-----------------

Handles music playback.
"""

import random
import os

from config import MUSIC_DIR, SUPPORTED_AUDIO_FILES
from commands.base import BaseCommand


class MusicCommand(BaseCommand):
    """
    Handles music playback.
    """

    def __init__(self, assistant):
        super().__init__(assistant)

    # ==========================================================
    # Play Music
    # ==========================================================

    def play_music(self, song_name: str | None = None) -> None:
        """
        Plays a song from the user's Music folder.

        Args:
            song_name (str | None): Optional song name.
        """

        if not MUSIC_DIR.exists():

            self.logger.error(
                "Music directory not found."
            )

            self.speech.speak(
                "I couldn't find your Music folder."
            )

            return

        songs = [
            song
            for song in MUSIC_DIR.iterdir()
            if song.is_file()
            and song.suffix.lower() in SUPPORTED_AUDIO_FILES
        ]

        if not songs:

            self.logger.warning(
                "No supported music files found."
            )

            self.speech.speak(
                "No music files were found."
            )

            return

        # Search by name
        if song_name:

            filtered = [
                song
                for song in songs
                if song_name.lower() in song.stem.lower()
            ]

            if filtered:
                songs = filtered
            else:

                self.speech.speak(
                    f"I couldn't find {song_name}."
                )

                return

        selected_song = random.choice(songs)

        self.logger.info(
            f"Playing: {selected_song.name}"
        )

        self.speech.speak(
            f"Playing {selected_song.stem}"
        )

        os.startfile(selected_song)