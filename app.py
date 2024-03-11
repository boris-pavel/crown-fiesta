from symbols import SEVEN, CHERRY, LEMON, PLUM, WATERMELON, STAR, ORANGE, GRAPE, DOLLAR, CROWN, BELL;
from flask import Flask, render_template, request
import random
from helpers import eliminate_column_duplicates, expand_crown;
SYMBOLS = [CROWN, STAR, DOLLAR, SEVEN, CHERRY, LEMON, PLUM, WATERMELON, ORANGE, GRAPE, BELL]


# Configure application
app = Flask(__name__)

# Set debug mode
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Generate slot
        game = []
        for i in range(3):
            line = []
            for j in range(5):
                l = SYMBOLS[:]
                if j == 0 or j == 4:
                    l.pop(0)
                    line.append(random.choice(l))
                elif j == 1 or j == 3:
                    l.pop(1)
                    line.append(random.choice(l))
                else:
                    line.append(random.choice(l))
            game.append(line)
        eliminate_column_duplicates(game)
        expand_crown(game)
        return render_template("index.html", game=game, balance=0)
    else:
        return render_template("index.html", game= [[SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                                                    [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                                                    [SEVEN, CROWN, BELL, ORANGE, CHERRY]], balance = 0)


if __name__ == '__main__':
    app.run(debug=True)
