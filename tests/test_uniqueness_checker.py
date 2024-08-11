from src.uniqueness_checker import UniquenessChecker

def test_check_unique_pairings():
    cards = [
        ("Python", "Ubuntu", "Alan Turing"),
        ("Java", "Fedora", "Grace Hopper"),
        ("C", "Debian", "Donald Knuth")
    ]
    checker = UniquenessChecker()
    
    assert checker.check_unique_pairings(cards)


def test_check_non_unique_pairings():
    cards = [
        ("Python", "Ubuntu", "Alan Turing"),
        ("Java", "Ubuntu", "Alan Turing"),  # Duplicate pairing
        ("C", "Debian", "Donald Knuth")
    ]
    checker = UniquenessChecker()
    
    assert not checker.check_unique_pairings(cards)