import os
from src.pdf_generator import PDFGenerator

def test_generate_pdf():
    cards = [
        ("Python", "Ubuntu", "Alan Turing"),
        ("Java", "Fedora", "Grace Hopper"),
        ("C", "Debian", "Donald Knuth")
    ]
    filename = "test_cards.pdf"
    pdf_gen = PDFGenerator(filename)
    pdf_gen.generate_pdf(cards)
    
    # Check if the PDF file is created
    assert os.path.exists(filename)
    
    # Cleanup
    os.remove(filename)

