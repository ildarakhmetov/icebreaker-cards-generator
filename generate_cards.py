from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from itertools import product
import random


# Create the lists of languages, distributions, and pioneers
LANGUAGES = ["Python", "Java", "C", "C++", "JavaScript", "Ruby", "Go"]
DISTRIBUTIONS = ["Ubuntu", "Fedora", "Debian", "Arch", "CentOS", "Mint", "SUSE"]
PIONEERS = ["Alan Turing", "Grace Hopper", "Donald Knuth", "Ada Lovelace",
            "Edsger Dijkstra", "Tim Berners-Lee", "Linus Torvalds"]

# Number of cards to generate
k = 36


def generate_unique_combinations(languages, distributions, pioneers, k):
    """
    Generates a list of k unique combinations where each pairing in the combination
    (language-distribution, distribution-pioneer, language-pioneer) is unique.
    """
    # Generate all possible combinations, shuffle them
    combinations = list(product(languages, distributions, pioneers))
    random.shuffle(combinations)

    unique_combinations = []
    used_pairs = set()

    # Keep generating combinations until we have k unique ones
    while len(unique_combinations) < k:
        # Randomly select a combination
        combo = random.choice(combinations)

        # Create pairs to check uniqueness
        pairs = [(combo[0], combo[1]), (combo[1], combo[2]), (combo[0], combo[2])]

        # Check if any pair has been used before
        if any(pair in used_pairs for pair in pairs):
            continue

        # Add the pairs to the used set and the combo to the unique list
        for pair in pairs:
            used_pairs.add(pair)
        unique_combinations.append(combo)

    return unique_combinations


def check_unique_pairings(cards):
    lang_dist_pairs = set()
    lang_pioneer_pairs = set()
    dist_pioneer_pairs = set()

    for (lang, dist, pioneer) in cards:
        # Check if the pair (language, distribution) is unique
        if (lang, dist) in lang_dist_pairs:
            return False
        lang_dist_pairs.add((lang, dist))

        # Check if the pair (language, pioneer) is unique
        if (lang, pioneer) in lang_pioneer_pairs:
            return False
        lang_pioneer_pairs.add((lang, pioneer))

        # Check if the pair (distribution, pioneer) is unique
        if (dist, pioneer) in dist_pioneer_pairs:
            return False
        dist_pioneer_pairs.add((dist, pioneer))

    # If no duplicates were found, the pairings are unique
    return True


def generate_pdf(cards, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter  # Default Letter size
    margin = inch * 0.5  # Margin of 0.5 inches
    card_width = (width - 2 * margin) / 4
    card_height = (height - 2 * margin) / 3
    font_size = 12  # Increased font size

    c.setFont("Helvetica", font_size)

    for i, (lang, dist, pioneer) in enumerate(cards):
        x = margin + (i % 4) * card_width
        y = height - margin - ((i // 4) % 3 + 1) * card_height
        c.rect(x, y, card_width, card_height)
        
        # Centering text horizontally and vertically
        text_height = font_size + 4  # Added padding
        total_text_height = 3 * text_height
        start_y = y + (card_height + total_text_height) / 2

        c.drawCentredString(x + card_width / 2, start_y - text_height, lang)
        c.drawCentredString(x + card_width / 2, start_y - 2 * text_height, dist)
        c.drawCentredString(x + card_width / 2, start_y - 3 * text_height, pioneer)

        if i % 12 == 11:
            c.showPage()

    c.save()


# Generate the cards
cards = generate_unique_combinations(LANGUAGES, DISTRIBUTIONS, PIONEERS, k)

# Check that all pairings are unique
is_unique = check_unique_pairings(cards)
print("All pairings are unique." if is_unique else "There are duplicate pairings.")

# Count the number of unique languages, distributions, and pioneers
languages = set()
distributions = set()
pioneers = set()
for (lang, dist, pioneer) in cards:
    languages.add(lang)
    distributions.add(dist)
    pioneers.add(pioneer)

# Count how many times each language, distribution, and pioneer appears
language_counts = {}
distribution_counts = {}
pioneer_counts = {}
for (lang, dist, pioneer) in cards:
    language_counts[lang] = language_counts.get(lang, 0) + 1
    distribution_counts[dist] = distribution_counts.get(dist, 0) + 1
    pioneer_counts[pioneer] = pioneer_counts.get(pioneer, 0) + 1

# Print the results
print("Language counts: {}".format(language_counts))
print("Distribution counts: {}".format(distribution_counts))
print("Pioneer counts: {}".format(pioneer_counts))

print("There are {} unique languages.".format(len(languages)))
print("There are {} unique distributions.".format(len(distributions)))
print("There are {} unique pioneers.".format(len(pioneers)))


# Generate PDF with your cards
generate_pdf(cards, "cards.pdf")