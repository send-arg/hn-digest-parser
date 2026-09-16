import json
import urllib.request
from datetime import datetime


def fetch_top_stories(limit: int = 5) -> list[dict]:
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req) as response:
        story_ids = json.loads(response.read().decode())[:limit]

    stories = []
    for story_id in story_ids:
        item_url = (
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        with urllib.request.urlopen(item_url) as item_resp:
            data = json.loads(item_resp.read().decode())
            stories.append(
                {
                    "title": data.get("title"),
                    "url": data.get("url", "https://news.ycombinator.com"),
                    "score": data.get("score", 0),
                    "author": data.get("by"),
                }
            )
    return stories


def export_digest():
    results = fetch_top_stories(limit=5)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"=== Hacker News Digest ({timestamp}) ===\n")
    for idx, story in enumerate(results, 1):
        print(f"{idx}. [{story['score']} pts] {story['title']}")
        print(f"   Link: {story['url']}\n")


if __name__ == "__main__":
    export_digest()
