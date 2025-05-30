"""Tests for code."""

from teamsservicebell import servicebell


def test_servicebell():
    """Put unittests here."""
    resp = servicebell.press_button()
    assert resp is None
