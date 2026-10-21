import feedparser


FEED_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


class FeedFetchError(RuntimeError):
    pass


def fetch_feed(url, parser=feedparser.parse):
    errors = []
    for kwargs in ({"agent": FEED_USER_AGENT}, {}):
        try:
            feed = parser(url, **kwargs)
        except Exception as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
            continue

        status = feed.get("status")
        if status is not None and status >= 400:
            errors.append(f"HTTP {status}")
            continue
        return feed

    raise FeedFetchError(f"Stažení {url} selhalo: {'; '.join(errors)}")


def iter_available_feeds(blogs, fetch=fetch_feed, warn=print):
    for blog in blogs:
        try:
            feed = fetch(blog["url"])
        except Exception as exc:
            warn(
                f"Zdroj {blog['name']} ({blog['url']}) přeskočen: "
                f"{type(exc).__name__}: {exc}"
            )
            continue
        yield blog, feed
