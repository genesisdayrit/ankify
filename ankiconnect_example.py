import requests
import json

# Define the deck and card content
deck_name = "My AnkiConnect Deck"
card = {
    "deckName": deck_name,
    "modelName": "Basic",
    "fields": {
        "Front": "What is the capital of Japan?",
        "Back": "Tokyo"
    },
    "tags": ["geography"]
}

# Send a request to AnkiConnect to create the card
def add_card(card):
    result = requests.post('http://localhost:8765', json.dumps({
        "action": "addNote",
        "version": 6,
        "params": {
            "note": card
        }
    }))
    return result.json()

# Create the deck if it doesn't already exist
def create_deck(deck_name):
    requests.post('http://localhost:8765', json.dumps({
        "action": "createDeck",
        "version": 6,
        "params": {
            "deck": deck_name
        }
    }))

# Ensure deck exists and add the card
create_deck(deck_name)
add_card(card)

