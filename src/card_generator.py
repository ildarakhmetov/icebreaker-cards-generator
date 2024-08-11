from itertools import product
import random
from typing import List, Tuple

class CardGenerator:
    def __init__(self, languages: List[str], distributions: List[str], pioneers: List[str], random_seed=None):
        self.languages = languages
        self.distributions = distributions
        self.pioneers = pioneers
        if random_seed is not None:
            random.seed(random_seed)

    def generate_unique_combinations(self, k: int, max_attempts: int = 1000) -> List[Tuple[str, str, str]]:
        """
        Generates a list of k unique combinations where each pairing in the combination
        (language-distribution, distribution-pioneer, language-pioneer) is unique.
        If it cannot find k unique combinations within max_attempts, it returns False.
        """
        combinations = list(product(self.languages, self.distributions, self.pioneers))
        random.shuffle(combinations)

        unique_combinations = []
        used_pairs = set()
        attempts = 0

        while len(unique_combinations) < k and attempts < max_attempts:
            combo = random.choice(combinations)
            pairs = [(combo[0], combo[1]), (combo[1], combo[2]), (combo[0], combo[2])]

            if any(pair in used_pairs for pair in pairs):
                attempts += 1
                continue

            for pair in pairs:
                used_pairs.add(pair)
            unique_combinations.append(combo)
            attempts = 0  # Reset attempts after a successful addition

        if len(unique_combinations) < k:
            return []

        return unique_combinations