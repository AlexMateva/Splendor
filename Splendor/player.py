from settings import CARD_TYPES, CHIP_TYPES
from collections import Counter
global ALL_GIVEN_CARDS_ON_TABLE
global ALL_GIVEN_CARDS


LEVEL1_CARDS_ON_TABLE = []
LEVEL2_CARDS_ON_TABLE = []
LEVEL3_CARDS_ON_TABLE = []
ALL_CARDS_ON_TABLE = []
ALL_CHIPS_ON_TABLE = {'Emerald': 0,
                      'Sapphire': 0,
                      'Ruby': 0,
                      'Diamond': 0,
                      'Onyx': 0,
                      'Gold': 0}


class Player:
    def __init__(self, name=None):
        self.name = name
        self.cards = []
        self.cards_value = {'Emerald': 0,
                            'Sapphire': 0,
                            'Ruby': 0,
                            'Diamond': 0,
                            'Onyx': 0}

        self.chips = {'Emerald': 0,
                      'Sapphire': 0,
                      'Ruby': 0,
                      'Diamond': 0,
                      'Onyx': 0,
                      'Gold': 0}
        self.points = 0
        self.resources = {"Diamond": 0,
                          "Sapphire": 0,
                          "Emerald": 0,
                          "Ruby": 0,
                          "Onyx": 0,
                          "Gold": 0}

    def card_types(self):
        return Counter([c.gem_type for c in self.cards])

    def can_take_three_chips(self):
        return len(self.chips) <= 7

    def can_take_two_chips(self):
        return len(self.chips) <= 8

    def add_card(self, card):
        ALL_CARDS_ON_TABLE.remove(card)
        if card.level == "_level1":
            LEVEL1_CARDS_ON_TABLE.remove(card)
        if card.level == "_level2":
            LEVEL2_CARDS_ON_TABLE.remove(card)
        if card.level == "_level3":
            LEVEL3_CARDS_ON_TABLE.remove(card)
        self.use_resourses(card)
        self.points += card.points
        self.cards.append(card)
        self.resources[card.gem_type] += 1

    def use_recourses(self, card):
        cards_value = self.card_types()
        for gems in card.cost:
            if cards_value[gems] >= card.cost[gems]:
                pass
            elif cards_value[gems] < card.cost[gems]:
                if self.chips[gems] + cards_value[gems] >= card.cost[gems]:
                    self.chips[gems] -= card.cost[gems] - cards_value[gems]
                    self.resources[gems] -= card.cost[gems] - cards_value[gems]
                else:
                    self.resources[gems] -= self.chips[gems]
                    self.chips[gems] = 0
                    self.resources["Gold"] -= card.cost[gems] - cards_value[gems] - self.chips[gems]
                    self.chips["Gold"] -= card.cost[gems] - cards_value[gems] - self.chips[gems]

    def add_chips(self, chips):
        for chip in chips:
            self.chips[chip.gem_type] += 1
            ALL_CHIPS_ON_TABLE[chip.gem_type] -= 1
            self.resources[chip.gem_type] += 1

    def can_buy_card(self, card):
        cards_value = self.card_types()
        gold_chips = self.chips["Gold"]
        for gems in card.cost:
            if self.resources[gems] >= card.cost[gems]:
                pass
            elif self.resources[gems] == card.cost[gems] - 1 and self.chips["Gold"] > 0:
                self.chips["Gold"] -= 1
            else:
                self.chips["Gold"] = gold_chips
                return False
        self.chips["Gold"] = gold_chips
        return True

    def buy_card(self, card):
        if self.can_buy_card(card):
            self.add_card(card)

    def won_game(self):
        return self.points >= 15

    def get_all_of_one_type(self, card_gem_type):
        return [c.gem_type for c in self.cards if c.gem_type == card_gem_type]

    def set_game(self, game):
        self.game_i_want = game

    def pregame_(self):
        possible_cards = []
        for card in ALL_CARDS_ON_TABLE:
            if self.can_buy_card(card):
                possible_cards.append(card)
        if possible_cards.empty():
            pass
