from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from typing import List, Tuple

class PDFGenerator:
    def __init__(self, filename: str, page_size=letter, margin=0.5 * inch, font_size=12):
        self.filename = filename
        self.page_size = page_size
        self.margin = margin
        self.font_size = font_size

    def generate_pdf(self, cards: List[Tuple[str, str, str]]) -> None:
        c = canvas.Canvas(self.filename, pagesize=self.page_size)
        width, height = self.page_size
        card_width = (width - 2 * self.margin) / 4
        card_height = (height - 2 * self.margin) / 3

        c.setFont("Helvetica", self.font_size)

        for i, (lang, dist, pioneer) in enumerate(cards):
            x = self.margin + (i % 4) * card_width
            y = height - self.margin - ((i // 4) % 3 + 1) * card_height
            c.rect(x, y, card_width, card_height)
            
            text_height = self.font_size + 4
            total_text_height = 3 * text_height
            start_y = y + (card_height + total_text_height) / 2

            c.drawCentredString(x + card_width / 2, start_y - text_height, lang)
            c.drawCentredString(x + card_width / 2, start_y - 2 * text_height, dist)
            c.drawCentredString(x + card_width / 2, start_y - 3 * text_height, pioneer)

            if i % 12 == 11:
                c.showPage()

        c.save()