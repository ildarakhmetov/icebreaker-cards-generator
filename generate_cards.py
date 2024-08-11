from src.card_generator import CardGenerator
from src.uniqueness_checker import UniquenessChecker
from src.statistics import Statistics
from src.pdf_generator import PDFGenerator
from config import LANGUAGES, DISTRIBUTIONS, PIONEERS, NUM_STUDENTS


if __name__ == "__main__":
    # Generate cards
    generator = CardGenerator(LANGUAGES, DISTRIBUTIONS, PIONEERS)
    cards = generator.generate_unique_combinations(NUM_STUDENTS)

    # Check uniqueness
    checker = UniquenessChecker()
    is_unique = checker.check_unique_pairings(cards)
    if not is_unique:
        print("Error: Duplicate pairings found")
        exit

    # Generate statistics
    language_counts, distribution_counts, pioneer_counts = Statistics.count_items(cards)
    print("Language counts:", language_counts)
    print("Distribution counts:", distribution_counts)
    print("Pioneer counts:", pioneer_counts)

    # Generate PDF
    pdf_gen = PDFGenerator("cards.pdf")
    pdf_gen.generate_pdf(cards)
