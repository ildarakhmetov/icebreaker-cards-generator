from src.statistics import Statistics

def test_count_items():
    cards = [
        ("Python", "Ubuntu", "Alan Turing"),
        ("Python", "Fedora", "Grace Hopper"),
        ("Java", "Ubuntu", "Alan Turing")
    ]
    
    language_counts, distribution_counts, pioneer_counts = Statistics.count_items(cards)
    
    expected_language_counts = {"Python": 2, "Java": 1}
    expected_distribution_counts = {"Ubuntu": 2, "Fedora": 1}
    expected_pioneer_counts = {"Alan Turing": 2, "Grace Hopper": 1}
    
    assert language_counts == expected_language_counts
    assert distribution_counts == expected_distribution_counts
    assert pioneer_counts == expected_pioneer_counts

