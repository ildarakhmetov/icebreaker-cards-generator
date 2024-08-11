import pytest
from itertools import product
from src.card_generator import CardGenerator

def test_generate_unique_combinations_two():
    languages = ["Python", "Java"]
    distributions = ["Ubuntu", "Fedora"]
    pioneers = ["Alan Turing", "Grace Hopper"]
    generator = CardGenerator(languages, distributions, pioneers, random_seed=42)
    
    combinations = generator.generate_unique_combinations(2)
    
    assert len(combinations) == 2
    
    # Ensure all generated combinations are within the expected cartesian product
    expected_combinations = set(product(languages, distributions, pioneers))
    for combo in combinations:
        assert combo in expected_combinations


def test_generate_unique_combinations_three():
    languages = ["Python", "Java", "C"]
    distributions = ["Ubuntu", "Fedora", "Debian"]
    pioneers = ["Alan Turing", "Grace Hopper", "Donald Knuth"]
    generator = CardGenerator(languages, distributions, pioneers, random_seed=42)
    
    combinations = generator.generate_unique_combinations(6)
    
    assert len(combinations) == 6
    
    # Ensure all generated combinations are within the expected cartesian product
    expected_combinations = set(product(languages, distributions, pioneers))
    for combo in combinations:
        assert combo in expected_combinations


def test_generate_combinations_large_k():
    languages = ["Python", "Java"]
    distributions = ["Ubuntu", "Fedora"]
    pioneers = ["Alan Turing", "Grace Hopper"]
    generator = CardGenerator(languages, distributions, pioneers, random_seed=42)
    
    # k is set larger than the possible unique combinations
    combinations = generator.generate_unique_combinations(100)
    
    # Ensure it returns the maximum possible unique combinations
    assert len(combinations) == 0


def test_generate_combinations_with_max_attempts():
    languages = ["Python", "Java"]
    distributions = ["Ubuntu", "Fedora"]
    pioneers = ["Alan Turing", "Grace Hopper"]
    generator = CardGenerator(languages, distributions, pioneers, random_seed=42)
    
    # Set k to a value that is impossible to achieve within the max_attempts
    combinations = generator.generate_unique_combinations(20, max_attempts=1000)
    
    # Ensure it returns fewer combinations due to max_attempts limit
    assert len(combinations) == 0


def test_generate_combinations_no_duplicates():
    languages = ["Python", "Java"]
    distributions = ["Ubuntu", "Fedora"]
    pioneers = ["Alan Turing", "Grace Hopper"]
    generator = CardGenerator(languages, distributions, pioneers, random_seed=42)
    
    combinations = generator.generate_unique_combinations(4)
    
    # Ensure no duplicate pairs in the combinations
    used_pairs = set()
    for combo in combinations:
        pairs = [(combo[0], combo[1]), (combo[1], combo[2]), (combo[0], combo[2])]
        for pair in pairs:
            assert pair not in used_pairs
            used_pairs.add(pair)
