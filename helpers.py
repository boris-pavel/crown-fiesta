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
            game[1][i] = random.choice(SYMBOLS)
        if x == z:
            game[0][i] = random.choice(SYMBOLS)
        if y == z:
            game[1][i] = random.choice(SYMBOLS)


def expand_crown(game):
    for i in range(1, 5):
        if game[0][i] == CROWN or game[1][i] == CROWN or game[2][i] == CROWN:
            game[0][i] = CROWN
            game[1][i] = CROWN
            game[2][i] = CROWN


def calculate_payline(symbol1, symbol2, symbol3, symbol4, symbol5, bet):
    if symbol1 not in [DOLLAR, STAR]:
        if symbol2 == CROWN:
            symbol2 = symbol1
        if symbol3 == CROWN:
            symbol3 = symbol1
        if symbol4 == CROWN:
            symbol4 = symbol1
        if symbol1 == symbol2 == symbol3:
            if symbol1 == symbol4:
                if symbol1 == symbol5:
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
    symbol4 = game[2][3]
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


def calculate_total_winnings(game, bet):
    winnings = 0
    winnings += calculate_payline_1(game, bet)
    winnings += calculate_payline_2(game, bet)
    winnings += calculate_payline_3(game, bet)
    winnings += calculate_payline_4(game, bet)
    winnings += calculate_payline_5(game, bet)
    winnings += calculate_payline_6(game, bet)
    winnings += calculate_payline_7(game, bet)
    winnings += calculate_payline_8(game, bet)
    winnings += calculate_payline_9(game, bet)
    return winnings
