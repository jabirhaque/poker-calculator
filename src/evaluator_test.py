import random
from evaluator import evaluate
from card import Card
def evaluate_random_hand():
    cards = [
        "AC", "AD", "AH", "AS",
        "KC", "KD", "KH", "KS",
        "QC", "QD", "QH", "QS",
        "JC", "JD", "JH", "JS",
        "TC", "TD", "TH", "TS",
        "9C", "9D", "9H", "9S",
        "8C", "8D", "8H", "8S",
        "7C", "7D", "7H", "7S",
        "6C", "6D", "6H", "6S",
        "5C", "5D", "5H", "5S",
        "4C", "4D", "4H", "4S",
        "3C", "3D", "3H", "3S",
        "2C", "2D", "2H", "2S",
    ]
    cards = [Card(string) for string in cards]
    hand = []
    for i in range(5):
        int = random.randrange(0, len(cards))
        card = cards[int]
        cards.pop(int)
        hand.append(card)
    return evaluate(hand)

for i in range(1000000):
    print(evaluate_random_hand())
