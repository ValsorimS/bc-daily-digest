import http.client

import pytest

from feed_fetcher import FeedFetchError, fetch_feed, iter_available_feeds


def test_fetch_feed_falls_back_to_default_agent_after_remote_disconnect():
    calls = []
    recovered_feed = {"status": 200, "entries": [object()]}

    def parser(url, **kwargs):
        calls.append((url, kwargs))
        if kwargs:
            raise http.client.RemoteDisconnected(
                "Remote end closed connection without response"
            )
        return recovered_feed

    result = fetch_feed("https://waldo.be/feed/", parser=parser)

    assert result is recovered_feed
    assert calls == [
        (
            "https://waldo.be/feed/",
            {"agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )},
        ),
        ("https://waldo.be/feed/", {}),
    ]


def test_fetch_feed_falls_back_after_http_error_response():
    calls = []
    unavailable_feed = {"status": 503, "entries": []}
    recovered_feed = {"status": 200, "entries": [object()]}

    def parser(url, **kwargs):
        calls.append(kwargs)
        return unavailable_feed if kwargs else recovered_feed

    result = fetch_feed("https://www.hougaard.com/feed/", parser=parser)

    assert result is recovered_feed
    assert calls == [
        {"agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )},
        {},
    ]


def test_fetch_feed_raises_when_both_agents_get_http_errors():
    responses = iter([
        {"status": 503, "entries": []},
        {"status": 503, "entries": []},
    ])

    with pytest.raises(FeedFetchError, match="HTTP 503"):
        fetch_feed(
            "https://www.hougaard.com/feed/",
            parser=lambda url, **kwargs: next(responses),
        )


def test_iter_available_feeds_skips_failed_source_and_continues():
    blogs = [
        {"name": "Waldo", "url": "https://waldo.be/feed/"},
        {"name": "Working", "url": "https://example.com/feed/"},
    ]
    working_feed = {"status": 200, "entries": [object()]}
    warnings = []

    def fetch(url):
        if "waldo.be" in url:
            raise http.client.RemoteDisconnected("connection closed")
        return working_feed

    results = list(iter_available_feeds(blogs, fetch=fetch, warn=warnings.append))

    assert results == [(blogs[1], working_feed)]
    assert warnings == [
        "Zdroj Waldo (https://waldo.be/feed/) přeskočen: "
        "RemoteDisconnected: connection closed"
    ]
