from __future__ import annotations
import csv
from pathlib import Path
from typing import List
from recommender import Item


def load_items(csv_path: str | Path) -> List[Item]:
    items: List[Item] = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags = [tag.strip() for tag in row['tags'].split('|') if tag.strip()]
            items.append(
                Item(
                    id=int(row['id']),
                    title=row['title'],
                    category=row['category'],
                    description=row['description'],
                    difficulty=row['difficulty'],
                    url=row['url'],
                    tags=tags,
                )
            )
    return items
