from src.model.card import Card
from src.model.game import Game
from src.service.calculator import probability

pocket = [Card('TD'), Card('3S')]
community = [Card('TH'), Card('4S'), Card('2C')]
opponent_num = 1
opponent_cards = []

game = Game(pocket, community, opponent_num, opponent_cards)
probability(game)