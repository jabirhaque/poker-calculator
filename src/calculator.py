import itertools
import random

from game import *
from card import *
from evaluator import evaluate
import copy

def probability(game):
    num = 5000
    win_count = 0
    draw_count = 0
    loss_count = 0
    for i in range(num):
        end_game = generate_gameplay(game)
        if(win(end_game) == 1):
            win_count += 1
        elif (win(end_game) == -1):
            loss_count += 1
        else:
            draw_count += 1
    print("P(WIN): ", 100*(win_count/num))
    print("P(DRAW): ", 100 * (draw_count / num))
    print("P(LOSS): ", 100 * (loss_count / num))
    return [100*(win_count/num), 100*(draw_count/num), 100*(loss_count/num)]

def win(game):
    player_set = game.pocket + game.community
    player_combo = itertools.combinations(player_set, 5)
    player_rating = 10000
    for combo in player_combo:
        rating = evaluate(combo)
        if rating < player_rating:
            player_rating = rating

    opponent_rating = 10000
    for pocket in game.opponent_cards:
        opponent_set = pocket + game.community
        opponent_combo = itertools.combinations(opponent_set, 5)
        for combo in opponent_combo:
            rating = evaluate(combo)
            if rating < opponent_rating:
                opponent_rating = rating

    if (player_rating < opponent_rating):
        return 1
    if (player_rating > opponent_rating):
        return -1
    else:
        return 0

def generate_gameplay(game):
    # takes a game and returns a valid gameplay
    filled_game = copy.deepcopy(game)
    deck = ["AC", "AD", "AH", "AS",
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
             "2C", "2D", "2H", "2S"]
    unused_cards = {}
    for card in deck:
        unused_cards[card] = Card(card)
    for card in (filled_game.pocket + filled_game.community):
        unused_cards.pop(card.string, None)

    for i in range(2-len(filled_game.pocket)):
        keys = list(unused_cards.keys())
        random_key = random.choice(keys)
        filled_game.pocket.append(Card(random_key))
        unused_cards.pop(random_key, None)

    for i in range(5-len(filled_game.community)):
        keys = list(unused_cards.keys())
        random_key = random.choice(keys)
        filled_game.community.append(Card(random_key))
        unused_cards.pop(random_key, None)

    for i in range(game.opponent_num):
        pocket = []
        for j in range(2):
            keys = list(unused_cards.keys())
            random_key = random.choice(keys)
            pocket.append(Card(random_key))
            unused_cards.pop(random_key, None)
        filled_game.opponent_cards.append(pocket)

    return filled_game

game = Game([], [], 9, [])
print(probability(game))