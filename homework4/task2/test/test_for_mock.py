import pytest
import requests

from homework4.task2.mock.mock import count_dots_on_i


def test_for_count_of_dots_monkey_path(monkeypatch):
    class MonkyPath_resp:
        text = "iiiiiii"

        def __init__(self, url):
            self.url = url

    monkeypatch.setattr(requests, "get", MonkyPath_resp)
    actual_result = count_dots_on_i("https://example.com/")

    assert actual_result == 7


def test_of_count_network_error(monkeypatch):
    def mock_connection_error(url):
        raise ValueError(f"Unreachable {url}")

    monkeypatch.setattr(requests, "get", mock_connection_error)

    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("https://something_wrong_error")
