import genanki

# Define a model for your cards (Note Types)
my_model = genanki.Model(
    1607392319,  # A unique ID for this model
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',  # Front side of the card
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',  # Back side of the card
        },
    ])

# Create a deck
my_deck = genanki.Deck(
    2059400110,  # A unique ID for this deck
    'My First Genanki Deck')

# Create a note (card) and add it to the deck
note = genanki.Note(
    model=my_model,
    fields=['What is the capital of France?', 'Paris'])
my_deck.add_note(note)

# Optionally, add another note
note2 = genanki.Note(
    model=my_model,
    fields=['Who wrote "Pride and Prejudice"?', 'Jane Austen'])
my_deck.add_note(note2)

# Save the deck as a .apkg file
genanki.Package(my_deck).write_to_file('output.apkg')

