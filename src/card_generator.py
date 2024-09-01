from typing import List, Tuple
import pulp

class CardGenerator:
    def __init__(self, languages: List[str], distributions: List[str], pioneers: List[str], random_seed=None):
        self.languages = languages
        self.distributions = distributions
        self.pioneers = pioneers

    def generate_unique_combinations(self, k: int, max_attempts: int = 1000) -> List[Tuple[str, str, str]]:
        """
        Generates a list of k unique combinations where each pairing in the combination
        (language-distribution, distribution-pioneer, language-pioneer) is unique.
        """
        # Initialize the ILP problem
        prob = pulp.LpProblem("UniqueCombinations", pulp.LpMaximize)

        # Create decision variables
        x = pulp.LpVariable.dicts("x", (self.languages, self.distributions, self.pioneers), cat='Binary')

        # Objective function: maximize the number of selected combinations
        prob += pulp.lpSum(x[l][d][p] for l in self.languages for d in self.distributions for p in self.pioneers)

        # Constraints to ensure unique pairs
        # (language, distribution) pairs
        for l in self.languages:
            for d in self.distributions:
                prob += pulp.lpSum(x[l][d][p] for p in self.pioneers) <= 1

        # (distribution, pioneer) pairs
        for d in self.distributions:
            for p in self.pioneers:
                prob += pulp.lpSum(x[l][d][p] for l in self.languages) <= 1

        # (language, pioneer) pairs
        for l in self.languages:
            for p in self.pioneers:
                prob += pulp.lpSum(x[l][d][p] for d in self.distributions) <= 1

        # Constraint to select exactly k combinations
        prob += pulp.lpSum(x[l][d][p] for l in self.languages for d in self.distributions for p in self.pioneers) == k

        # Relaxed constraints to ensure each language is used approximately equally (within ±2)
        for l in self.languages:
            prob += (pulp.lpSum(x[l][d][p] for d in self.distributions for p in self.pioneers) >= (k // len(self.languages)) - 1)
            prob += (pulp.lpSum(x[l][d][p] for d in self.distributions for p in self.pioneers) <= (k // len(self.languages)) + 1)

        # Relaxed constraints to ensure each distribution is used approximately equally (within ±2)
        for d in self.distributions:
            prob += (pulp.lpSum(x[l][d][p] for l in self.languages for p in self.pioneers) >= (k // len(self.distributions)) - 1)
            prob += (pulp.lpSum(x[l][d][p] for l in self.languages for p in self.pioneers) <= (k // len(self.distributions)) + 1)

        # Relaxed constraints to ensure each pioneer is used approximately equally (within ±2)
        for p in self.pioneers:
            prob += (pulp.lpSum(x[l][d][p] for l in self.languages for d in self.distributions) >= (k // len(self.pioneers)) - 1)
            prob += (pulp.lpSum(x[l][d][p] for l in self.languages for d in self.distributions) <= (k // len(self.pioneers)) + 1)

        # Solve the ILP problem
        prob.solve()

        # Collect the results
        if prob.status == pulp.LpStatusOptimal:
            result = []
            for l in self.languages:
                for d in self.distributions:
                    for p in self.pioneers:
                        if pulp.value(x[l][d][p]) == 1:
                            result.append((l, d, p))
            return result
        else:
            # If no optimal solution is found or the problem is infeasible
            return []
