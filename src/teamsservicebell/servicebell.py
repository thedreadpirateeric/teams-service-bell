"""Teams Service Bell."""
import tkinter as tk
from typing import Any, Callable
import logging

import pymsteams

from .utils import _load_yaml

LOGGER = logging.getLogger("teamsservicebell")
PREFS = _load_yaml()


def send_message(webhookURI: str | None,
                 message: str | None) -> str | Callable[[], Any]:
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
    webhookURI = PREFS.get("webhookURI")
    message = PREFS.get("message")
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
