"""Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will
  cause problems: the code will get executed twice:

  - When you run `python -m bslib` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``bslib.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``bslib.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration

"""
from .servicebell import main_window


def main():
    """Run the main.

    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    """
    main_window()
    return 0
