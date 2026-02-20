#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "beautifulsoup4==4.12.3",
#   "feedparser==6.0.11",
#   "python-dateutil==2.9.0.post0",
#   "requests==2.32.3",
# ]
# ///

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
import html

import feedparser
import requests
from bs4 import BeautifulSoup
from dateutil import parser as date_parser


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch podcast RSS and generate episodes JSON."
    )
    parser.add_argument("--rss-url", required=True, help="Podcast RSS feed URL")
    parser.add_argument(
        "--out",
        default="resources/episodes.json",
        help="Output JSON path (default: resources/episodes.json)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional max number of episodes for testing",
    )
    return parser.parse_args()


def iso_utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def to_iso_datetime(entry):
    if entry.get("published_parsed"):
        dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")
    if entry.get("updated_parsed"):
        dt = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")
    raw = entry.get("published") or entry.get("updated")
    if not raw:
        return None
    try:
        dt = date_parser.parse(raw)
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    except (ValueError, TypeError):
        return None


def strip_html(value):
    if not value:
        return ""
    soup = BeautifulSoup(value, "html.parser")
    text = soup.get_text(" ", strip=True)
    return html.unescape(text)


def parse_duration(value):
    if value is None:
        return None
    if isinstance(value, int):
        return value
    value = str(value).strip()
    if not value:
        return None
    if value.isdigit():
        return int(value)
    parts = [part for part in value.split(":") if part.isdigit()]
    if not parts:
        return None
    try:
        parts = [int(part) for part in parts]
    except ValueError:
        return None
    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds
    return None


def build_episode_id(entry, audio_url, published):
    guid = entry.get("id") or entry.get("guid")
    if guid:
        return str(guid)
    title = entry.get("title", "")
    base = f"{title}|{published or ''}|{audio_url or ''}"
    return hashlib.sha256(base.encode("utf-8")).hexdigest()


def extract_audio_url(entry):
    enclosures = entry.get("enclosures") or []
    for enclosure in enclosures:
        url = enclosure.get("url")
        if url:
            return url
    return None


def normalize_entry(entry):
    published = to_iso_datetime(entry)
    audio_url = extract_audio_url(entry)
    description = strip_html(entry.get("summary") or entry.get("description") or "")
    duration = parse_duration(entry.get("itunes_duration"))
    return {
        "id": build_episode_id(entry, audio_url, published),
        "title": (entry.get("title") or "").strip(),
        "description": description,
        "published": published,
        "link": entry.get("link"),
        "audio_url": audio_url,
        "duration": duration,
    }


def fetch_feed(rss_url):
    response = requests.get(rss_url, timeout=30)
    response.raise_for_status()
    return feedparser.parse(response.content)


def main():
    args = parse_args()
    feed = fetch_feed(args.rss_url)

    podcast_title = feed.feed.get("title") or "Podcast"
    episodes = [normalize_entry(entry) for entry in feed.entries]

    if args.limit is not None:
        episodes = episodes[: args.limit]

    episodes = [episode for episode in episodes if episode.get("title")]

    def sort_key(item):
        published = item.get("published")
        if not published:
            return 0
        try:
            return datetime.fromisoformat(published.replace("Z", "+00:00")).timestamp()
        except ValueError:
            return 0

    episodes.sort(key=sort_key, reverse=True)

    payload = {
        "podcast": {
            "title": podcast_title,
            "source_rss": args.rss_url,
            "generated_at": iso_utc_now(),
        },
        "episodes": episodes,
    }

    out_path = args.out
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=True)
        handle.write("\n")

    print(f"Wrote {len(episodes)} episodes to {out_path}")


if __name__ == "__main__":
    main()
