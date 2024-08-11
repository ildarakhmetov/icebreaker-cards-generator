from typing import List, Tuple, Dict

class Statistics:
    @staticmethod
    def count_items(cards: List[Tuple[str, str, str]]) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
        language_counts = {}
        distribution_counts = {}
        pioneer_counts = {}

        for (lang, dist, pioneer) in cards:
            language_counts[lang] = language_counts.get(lang, 0) + 1
            distribution_counts[dist] = distribution_counts.get(dist, 0) + 1
            pioneer_counts[pioneer] = pioneer_counts.get(pioneer, 0) + 1

        return language_counts, distribution_counts, pioneer_counts