import os
from src.card_generator import CardGenerator
from src.uniqueness_checker import UniquenessChecker
from src.pdf_generator import PDFGenerator

def test_full_integration():
    languages = ["Python", "Java", "C"]
    distributions = ["Ubuntu", "Fedora", "Debian"]
    pioneers = ["Alan Turing", "Grace Hopper", "Donald Knuth"]

    generator = CardGenerator(languages, distributions, pioneers, random_seed=42)
    cards = generator.generate_unique_combinations(9)
    
    checker = UniquenessChecker()
    assert checker.check_unique_pairings(cards)
    
    filename = "test_integration.pdf"
    pdf_gen = PDFGenerator(filename)
    pdf_gen.generate_pdf(cards)
    
    # Check if the PDF file is created
    assert os.path.exists(filename)
    
    # Cleanup
    os.remove(filename)

