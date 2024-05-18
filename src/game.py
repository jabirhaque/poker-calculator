class Game:
    def __init__(self, pocket, community, opponent_num, opponent_cards):
        self.pocket = pocket
        self.community = community
        self.opponent_cards = opponent_cards
        self.opponent_num = opponent_num
        if len(community) == 0:
            self.state = "pre-flop"
        elif len(community) == 3:
            self.state = "flop"
        elif len(community) == 4:
            self.state = "turn"
        else:
            self.state = "river"
    def print_game(self):
        print("game state: ", self.state)
        print("number of opponents: ", self.opponent_num)
        print("player cards:")
        print("    ", self.pocket[0].string, self.pocket[1].string)
        print("community cards:")
        print("    ", end = " ")
        for card in self.community:
            print(card.string, end = " ")
        print()
        if len(self.opponent_cards) != 0:
            print("opponent cards:")
            for i in range(len(self.opponent_cards)):
                print("    ", self.opponent_cards[i][0].string, self.opponent_cards[i][1].string)