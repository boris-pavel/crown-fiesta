from symbols import (
    SEVEN,
    CHERRY,
    LEMON,
    PLUM,
    WATERMELON,
    ORANGE,
    GRAPE,
    BELL,
    CROWN,
    DOLLAR,
    STAR,
    Symbol
)
import random


SYMBOLS = [SEVEN, CHERRY, LEMON, PLUM, WATERMELON, ORANGE, GRAPE, BELL]


def eliminate_column_duplicates(game):
    # For stars, crowns, dollars
    for i in range(5):
        x = game[0][i]
        y = game[1][i]
        z = game[2][i]
        if x == y:
            choice = random.choice(SYMBOLS)
            el = Symbol(choice.name, choice.path, choice.points)
            game[1][i] = el
        if x == z:
            choice = random.choice(SYMBOLS)
            el = Symbol(choice.name, choice.path, choice.points)
            game[0][i] = el
        if y == z:
            choice = random.choice(SYMBOLS)
            el = Symbol(choice.name, choice.path, choice.points)
            game[1][i] = el


def expand_crown(game):
    for i in range(1, 5):
        if game[0][i] == CROWN or game[1][i] == CROWN or game[2][i] == CROWN:
            game[0][i] = Symbol(CROWN.name, CROWN.path, CROWN.points)
            game[1][i] = Symbol(CROWN.name, CROWN.path, CROWN.points)
            game[2][i] = Symbol(CROWN.name, CROWN.path, CROWN.points)


def calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet):
    symbol2_crown = False
    symbol3_crown = False
    symbol4_crown = False
    # Check if in paying symbols
    if symbol1 not in [DOLLAR, STAR]:
        # If symbols 2,3,4 are CROWNS substitute them
        if symbol2 == CROWN:
            symbol2_crown = symbol2
            symbol2 = Symbol(symbol1.name, symbol1.path, symbol1.points)
        if symbol3 == CROWN:
            symbol3_crown = symbol3
            symbol3 = Symbol(symbol1.name, symbol1.path, symbol1.points)
        if symbol4 == CROWN:
            symbol4_crown = symbol4
            symbol4 = Symbol(symbol1.name, symbol1.path, symbol1.points)
        if symbol1 == symbol2 == symbol3:
            symbol1.win = True
            symbol2.win = True
            symbol3.win = True
            if symbol2_crown:
                symbol2_crown.win = True
            if symbol3_crown:
                symbol3_crown.win = True
            if symbol1 == symbol4:
                symbol4.win = True
                if symbol4_crown:
                    symbol4_crown.win = True
                if symbol1 == symbol5:
                    symbol5.win = True
                    return bet * 5 * symbol1.points
                return bet * 4 * symbol1.points
            return bet * 3 * symbol1.points
    return 0


def calculate_payline_1(game, bet):
    symbol1 = game[0][0]
    symbol2 = game[0][1]
    symbol3 = game[0][2]
    symbol4 = game[0][3]
    symbol5 = game[0][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_2(game, bet):
    symbol1 = game[1][0]
    symbol2 = game[1][1]
    symbol3 = game[1][2]
    symbol4 = game[1][3]
    symbol5 = game[1][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_3(game, bet):
    symbol1 = game[2][0]
    symbol2 = game[2][1]
    symbol3 = game[2][2]
    symbol4 = game[2][3]
    symbol5 = game[2][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_4(game, bet):
    symbol1 = game[0][0]
    symbol2 = game[1][1]
    symbol3 = game[2][2]
    symbol4 = game[1][3]
    symbol5 = game[1][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_5(game, bet):
    symbol1 = game[2][0]
    symbol2 = game[1][1]
    symbol3 = game[0][2]
    symbol4 = game[1][3]
    symbol5 = game[2][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_6(game, bet):
    symbol1 = game[0][0]
    symbol2 = game[0][1]
    symbol3 = game[1][2]
    symbol4 = game[0][3]
    symbol5 = game[0][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_7(game, bet):
    symbol1 = game[2][0]
    symbol2 = game[2][1]
    symbol3 = game[1][2]
    symbol4 = game[2][3]
    symbol5 = game[2][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_8(game, bet):
    symbol1 = game[1][0]
    symbol2 = game[2][1]
    symbol3 = game[2][2]
    symbol4 = game[2][3]
    symbol5 = game[1][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_payline_9(game, bet):
    symbol1 = game[1][0]
    symbol2 = game[0][1]
    symbol3 = game[0][2]
    symbol4 = game[0][3]
    symbol5 = game[1][4]
    return calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet)


def calculate_winnings(game, bet):
    paylines = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    paylines[0] += calculate_payline_1(game, bet)
    paylines[1] += calculate_payline_2(game, bet)
    paylines[2] += calculate_payline_3(game, bet)
    paylines[3] += calculate_payline_4(game, bet)
    paylines[4] += calculate_payline_5(game, bet)
    paylines[5] += calculate_payline_6(game, bet)
    paylines[6] += calculate_payline_7(game, bet)
    paylines[7] += calculate_payline_8(game, bet)
    paylines[8] += calculate_payline_9(game, bet)
    return paylines


def clear_winnings(game):
    for line in game:
        for symbol in line:
            symbol.win = False
