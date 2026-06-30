"""
main.py
-------

Entry point for Karen Voice Assistant.
"""

from core.assistant import KarenAssistant


def main() -> None:
    """
    Starts Karen Voice Assistant.
    """

    assistant = None

    try:

        assistant = KarenAssistant()

        assistant.run()

    except KeyboardInterrupt:

        if assistant:

            assistant.logger.info(
                "Karen stopped by user."
            )

        print("\nKaren stopped by user.")

    except Exception as error:

        if assistant:

            assistant.logger.error(
                f"Fatal error: {error}"
            )

        print(
            f"\nFatal Error: {error}"
        )


if __name__ == "__main__":

    main()