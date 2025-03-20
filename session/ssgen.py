import os
from time import sleep

# Banner for the script
BANNER = r"""
┏━━━┳━━━┳━━━┳┓┏━┳━━━┳━━━┳┓╋┏┓
┗┓┏┓┃┏━┓┃┏━┓┃┃┃┏┫┏━┓┃┏━┓┃┃╋┃┃
╋┃┃┃┃┃╋┃┃┗━┛┃┗┛┛┃┗━━┫┗━━┫┗━┛┃
╋┃┃┃┃┗━┛┃┏┓┏┫┏┓┃┗━━┓┣━━┓┃┏━┓┃
┏┛┗┛┃┏━┓┃┃┃┗┫┃┃┗┫┗━┛┃┗━┛┃┃╋┃┃
┗━━━┻┛╋┗┻┛┗━┻┛┗━┻━━━┻━━━┻┛╋┗┛
"""

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def spinner():
    """Display a spinner animation while checking for Telethon."""
    print("Checking if Telethon is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print(f"\r{frame}", end="", flush=True)
            sleep(0.1)
    print("\r", end="")

def get_api_credentials():
    """Prompt the user for their API ID and API HASH."""
    print(
        "To generate a Telegram session string, you need your API ID and API HASH.\n"
        "Get these from https://my.telegram.org or @ScrapperRoBot.\n"
    )
    try:
        api_id = int(input("Enter your API ID: "))
    except ValueError:
        print("API ID must be an integer. Exiting...")
        exit(1)
    api_hash = input("Enter your API HASH: ")
    return api_id, api_hash

def generate_session():
    """Generate a Telegram session string using Telethon."""
    try:
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
        )
        from telethon.sessions import StringSession
        from telethon.sync import TelegramClient
    except ImportError:
        print("Telethon not found. Installing...")
        os.system("pip install -U telethon")
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
        )
        from telethon.sessions import StringSession
        from telethon.sync import TelegramClient

    api_id, api_hash = get_api_credentials()

    try:
        with TelegramClient(StringSession(), api_id, api_hash) as client:
            print("Generating session string...")
            session_string = client.session.save()
            client.send_message(
                "me",
                f"**DARKSSH Session String**:\n\n`{session_string}`\n\n"
                "**Do not share this with anyone!**",
            )
            print(
                "Session string generated and sent to your Telegram 'Saved Messages'."
            )
    except ApiIdInvalidError:
        print("Invalid API ID or API HASH. Please check your credentials.")
    except PhoneNumberInvalidError:
        print("Invalid phone number. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the script."""
    clear_screen()
    print(BANNER)
    generate_session()
    if input("Run again? (y/n): ").lower() == "y":
        main()
    else:
        print("Exiting...")
        exit(0)

if __name__ == "__main__":
    main()
