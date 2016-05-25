import random
import json
from settings import CARD_TYPES, CHIP_TYPES


class Card:
    def __init__(self, cost, gem_type, level, points=0):
        self.cost = cost
        self.gem_type = gem_type
        self.level = "_level" + str(level)
        self.points = points

    def __str__(self):
        return "'{}' costs {} and brings you {} points.".format(self.gem_type, self.cost, self.points)


class Chip:
    def __init__(self, gem_type):
        self.gem_type = gem_type


class Noble_tiles:
    def __init__(self, cost):
        self.cost = cost


class Deck:
    def __init__(self, level1, level2, level3):
        self._level1 = level1
        self._level2 = level2
        self._level3 = level3

    def save(self, json_filename):
        with open(json_filename, "w") as json_file:
            json_file.write(self._to_json())

    @staticmethod
    def load(json_filename):
        with open(json_filename, "r") as json_file:
            obj = json.load(json_file)

            decks = Deck(obj["_level1"], obj["_level2"], obj["_level3"])
            for card in obj["_level1"]:
                c = Card(card["cost"], card["gem_type"], card["level"], card["points"])
            for card in obj["_level2"]:
                c = Card(card["cost"], card["gem_type"], card["level"], card["points"])
            for card in obj["_level1"]:
                c = Card(card["cost"], card["gem_type"], card["level"], card["points"])
            return decks

    def _to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __getitem__(self, key):
        return self.deck[key]

    def __str__(self):
        return str([str(c) for c in self._level1] +
                   [str(c) for c in self._level2] +
                   [str(c) for c in self._level2])

    def add_card(self, card, level):
        self.__dict__["_" + level].append(card)

    def shuffle(self):
        random.shuffle(self._level1)
        random.shuffle(self._level2)
        random.shuffle(self._level3)

    def remove(self, cards):
        for c in cards:
            if c.level == "_level1" and c in self._level1:
                self._level1.remove(c)
            if c.level == "_level2" and c in self._level2:
                self._level1.remove(c)
            if c.level == "_level3" and c in self._level3:
                self._level1.remove(c)

