"""Utilities."""
import logging
import yaml
LOGGER = logging.getLogger("teamsservicebell")


def _load_yaml():
    """Open ini file for information for teams."""
    resp = {}
    try:
        stream = open("values.yaml", encoding="utf-8")
    except FileNotFoundError:
        stream = None
    else:
        with stream:
            try:
                resp = yaml.safe_load(stream)
                LOGGER.debug(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                LOGGER.exception(exc)
    return resp
