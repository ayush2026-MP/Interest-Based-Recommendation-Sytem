from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Tuple
import math

@dataclass
class Item:
    id: int
    title: str
    category: str
    description: str
    difficulty: str
    url: str
    tags: List[str]


class InterestBasedRecommender:
    def __init__(self, items: List[Item]):
        self.items = items

    @staticmethod
    def _normalize(text: str) -> str:
        return text.strip().lower()

    def score_item(self, selected_interests: List[str], item: Item) -> Tuple[float, Dict[str, float]]:
        normalized = {self._normalize(x) for x in selected_interests}
        item_tags = {self._normalize(x) for x in item.tags}

        tag_overlap = len(normalized & item_tags)
        tag_union = len(normalized | item_tags) or 1
        jaccard = tag_overlap / tag_union

        exact_match_bonus = 0.15 if tag_overlap > 0 else 0.0
        category_bonus = 0.10 if self._normalize(item.category) in normalized else 0.0

        score = min(1.0, jaccard + exact_match_bonus + category_bonus)
        details = {
            "jaccard_similarity": round(jaccard, 3),
            "exact_match_bonus": round(exact_match_bonus, 3),
            "category_bonus": round(category_bonus, 3),
            "final_score": round(score, 3),
        }
        return score, details

    def recommend(self, selected_interests: List[str], top_k: int = 5) -> List[Dict]:
        ranked = []
        for item in self.items:
            score, details = self.score_item(selected_interests, item)
            if score > 0:
                ranked.append({
                    "item": item,
                    "score": round(score, 3),
                    "details": details,
                })

        ranked.sort(key=lambda x: (-x["score"], x["item"].title))
        return ranked[:top_k]
