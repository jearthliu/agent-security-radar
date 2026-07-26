#!/usr/bin/env python3
"""Validate the public agent-security paper catalog."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_PAPER_FIELDS = {
    "arxiv_id",
    "title",
    "submitted",
    "lifecycle_stages",
    "url",
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    papers = payload.get("papers")

    if not isinstance(papers, list):
        fail("'papers' must be a list")
    if len(papers) != 5:
        fail(f"expected exactly 5 papers, found {len(papers)}")

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()

    for index, paper in enumerate(papers, start=1):
        if not isinstance(paper, dict):
            fail(f"paper {index} must be an object")

        missing = REQUIRED_PAPER_FIELDS - paper.keys()
        if missing:
            fail(f"paper {index} missing fields: {sorted(missing)}")

        arxiv_id = paper["arxiv_id"]
        url = paper["url"]
        submitted = paper["submitted"]
        stages = paper["lifecycle_stages"]

        if arxiv_id in seen_ids:
            fail(f"duplicate arXiv id: {arxiv_id}")
        if url in seen_urls:
            fail(f"duplicate source URL: {url}")

        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != "arxiv.org":
            fail(f"paper {index} must use a direct HTTPS arXiv source")
        if not parsed.path.endswith(arxiv_id):
            fail(f"paper {index} URL does not match arXiv id")
        if not isinstance(stages, list) or not stages:
            fail(f"paper {index} requires at least one lifecycle stage")

        date.fromisoformat(submitted)
        seen_ids.add(arxiv_id)
        seen_urls.add(url)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/papers.json")
    try:
        validate(path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"catalog invalid: {exc}", file=sys.stderr)
        return 1

    print(f"catalog valid: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())