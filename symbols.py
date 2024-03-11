
class Symbol:
    """A class for symbols on the reels"""
    def __init__(self, name, path, points):
        self.name = name
        self.path = path
        self.points = points

    def __eq__(self, other):
        return self.name == other.name

SEVEN = Symbol("seven", "static/symbols/7.png", 50)
CHERRY = Symbol("cherry", "static/symbols/cherries.png", 10)
LEMON = Symbol("lemon", "static/symbols/lemon.png", 10)
PLUM = Symbol("plum", "static/symbols/plum.png", 10)
BELL = Symbol("bell", "static/symbols/bell.png", 20)
WATERMELON = Symbol("watermelon", "static/symbols/watermelon.png", 40)
GRAPE = Symbol("grape", "static/symbols/grape.png", 40)
ORANGE = Symbol("orange", "static/symbols/orange.png", 10)
DOLLAR = Symbol("dollar", "static/symbols/dollar.png", 200)
STAR = Symbol("star", "static/symbols/star.png", 800)
CROWN = Symbol("crown", "static/symbols/crown.png", 10)
