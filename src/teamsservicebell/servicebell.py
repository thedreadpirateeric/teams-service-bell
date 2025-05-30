"""Teams Service Bell."""
import os
import tkinter as tk
from typing import Any, Callable

import pymsteams


def send_message(webhookURI: str, message: str) -> str | Callable[[], Any]:
    """Send a message to a teams webook.

    For more advanced features, see
        https://pypi.org/project/pymsteams/

    Args:
        webhookURI: webhook given from webhook connector.
        message: Body text of the teams message.

    Kwargs:
        Addtional kwags can be used as needed, given is an example.
    """
    myTeamsMessage = pymsteams.connectorcard(webhookURI)
    myTeamsMessage.text(message)
    return myTeamsMessage.send()


def press_button() -> None:
    """This would be the button press action."""
    webhookURI = os.getenv("TEAMS_WEBHOOK")
    message = ""
    if webhookURI:
        send_message(webhookURI, message)


def main_window():
    """This is the main app window."""
    # Create main window
    window = tk.Tk()
    window.title("Helpdesk Service Bell")

    # Create button widget
    button = tk.Button(window, text="Press For Help", command=press_button)
    button.pack(pady=20, padx=20)  # Add some padding

    # Start the Tkinter event loop
    window.mainloop()
