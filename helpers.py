from symbols import SEVEN, CHERRY, LEMON, PLUM, WATERMELON, ORANGE, GRAPE, BELL, CROWN;
import random


SYMBOLS = [SEVEN, CHERRY, LEMON, PLUM, WATERMELON, ORANGE, GRAPE, BELL]


def eliminate_column_duplicates(game):
    # For stars, crowns, dollars
    for i in range(5):
        x = game[0][i]
        y = game[1][i]
        z = game[2][i]
        if x == y:
            game[1][i] = random.choice(SYMBOLS)
        if x == z:
            game[0][i] = random.choice(SYMBOLS)
        if y == z:
            game[1][i] = random.choice(SYMBOLS)

def expand_crown(game):
    for i in range(1,5):
        if game[0][i] == CROWN or game[1][i] == CROWN or game[2][i] == CROWN:
            game[0][i] = CROWN
            game[1][i] = CROWN
            game[2][i] = CROWN
