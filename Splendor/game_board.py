GEM_TYPES = ['Emerald', 'Sapphire', 'Ruby', 'Diamond', 'Onyx']
CHIP_TYPES = ['Emerald', 'Sapphire', 'Ruby', 'Diamond', 'Onyx', 'Gold']


class Card:
    def __init__(self, cost, gem_type, level, points=0):
        self.cost = cost
        self.gem_type = gem_type
        self.level = "_level" + str(level)
        self.points = points


class Chip:
    def __init__(self, gem_type):
        self.gem_type = gem_type


class Lord:
    def __init__(self, cost):
        self.cost = cost


class SplendorTable:
    def __init__(self):
        name = 'a'
        score, br = 0, 0
        self.state = [[Card({'Emerald': 1, 'Sapphire': 2}, 'Emerald', 1),
                       Card({'Emerald': 1, 'Sapphire': 2}, 'Diamond', 1),
                       Card({'Emerald': 1, 'Sapphire': 2}, 'Sapphire', 1),
                       Card({'Emerald': 1, 'Sapphire': 2}, 'Ruby', 1),
                       [Chip('Ruby'), 2], [Chip('Ruby'), 1],
                       [Lord({'Emerald': 1, 'Sapphire': 2})], [Lord({'Emerald': 1, 'Sapphire': 2})]],
                      [Card({'Emerald': 1, 'Sapphire': 2}, 'Onyx', 1),
                       Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                       Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                      Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                      [Chip('Ruby'), 2], [Chip('Ruby'), 1],
                      [Lord({'Emerald': 1, 'Sapphire': 2})], [Lord({'Emerald': 1, 'Sapphire': 2})]],
                      [Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                      Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                      Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                      Card({'Emerald': 1, 'Sapphire': 2}, '1', 1),
                      [Chip('Ruby'), 2], [Chip('Ruby'), 1],
                      [Lord({'Emerald': 1, 'Sapphire': 2})], [Lord({'Emerald': 1, 'Sapphire': 2})]],
                      [name, [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br]],
                      [score, [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br],
                      [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br]],

                      [name, [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br]],
                      [score, [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br],
                      [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br]],

                      [name, [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br]],
                      [score, [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br],
                      [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br]],

                      [name, [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br], [GEM_TYPES[0], br]],
                      [score, [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br],
                      [CHIP_TYPES[0], br], [CHIP_TYPES[0], br], [CHIP_TYPES[0], br]]]

    def change_card(self, new_card, index):
        self.state[index(0)][index(1)] = new_card

