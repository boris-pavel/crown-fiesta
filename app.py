import random
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from helpers import (
    eliminate_column_duplicates,
    expand_crown,
    calculate_winnings,
    clear_winnings,
)
from symbols import (
    SEVEN,
    CHERRY,
    LEMON,
    PLUM,
    WATERMELON,
    STAR,
    ORANGE,
    GRAPE,
    DOLLAR,
    CROWN,
    BELL,
    Symbol,
)

SYMBOLS = [
    CROWN,
    STAR,
    DOLLAR,
    SEVEN,
    CHERRY,
    LEMON,
    PLUM,
    WATERMELON,
    ORANGE,
    GRAPE,
    BELL,
]


# Configure application
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///crown.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Generate slot
        if "user_id" not in session.keys():
            return render_template(
                "index_error.html",
                game=[
                    [SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                    [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                    [SEVEN, CROWN, BELL, ORANGE, CHERRY],
                ],
                error="You must log in to play.",
            )
        game = []
        bet = float(request.form.get("bet"))
        balance = db.execute(
            "SELECT balance FROM users WHERE id = ?", session["user_id"]
        )[0]["balance"]
        if bet < 0:
            return render_template(
                "game_error.html",game=[
                [SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                [SEVEN, CROWN, BELL, ORANGE, CHERRY]],
                error="Bet must be a positive integer",
                bet=bet,
                balance=balance,
            )

        if bet > balance:
            return render_template(
                "game_error.html",
                game=[
                    [SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                    [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                    [SEVEN, CROWN, BELL, ORANGE, CHERRY],
                ],
                error="Not enough funds.",
                balance=balance,
                bet=bet,
            )

        for i in range(3):
            line = []
            for j in range(5):
                l = SYMBOLS[:]
                # Check for crowns on columns 1 and 5
                if j == 0 or j == 4:
                    l.pop(0)
                    choice = random.choice(l)
                    el = Symbol(choice.name, choice.path, choice.points)
                    line.append(el)
                # Check for stars on columns 2 and 4
                elif j == 1 or j == 3:
                    l.pop(1)
                    choice = random.choice(l)
                    el = Symbol(choice.name, choice.path, choice.points)
                    line.append(el)
                else:
                    choice = random.choice(l)
                    el = Symbol(choice.name, choice.path, choice.points)
                    line.append(el)
            game.append(line)
        eliminate_column_duplicates(game)
        expand_crown(game)
        clear_winnings(game)
        win = round(sum(calculate_winnings(game, bet)), 2)
        balance = round(balance - bet + win, 2)

        db.execute(
            "UPDATE users SET balance = ? WHERE id = ?", balance, session["user_id"]
        )
        db.execute("UPDATE users SET bet = ? WHERE id = ?", bet, session["user_id"])
        db.execute(
            "INSERT INTO transactions (user_id, bet, win, date) VALUES(?, ?, ?, CURRENT_TIME)",
            session["user_id"],
            bet,
            win,
        )
        return render_template(
            "game.html", game=game, balance=balance, win=win, bet=bet
        )
    else:
        if "user_id" in session.keys() and session["user_id"] in db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        ):
            balance = db.execute(
                "SELECT balance FROM users WHERE id = ?", session["user_id"]
            )[0]["balance"]
            bet = db.execute("SELECT bet FROM users WHERE id = ?", session["user_id"])[
                0
            ]["bet"]
            return render_template(
                "game.html",
                game=[
                    [SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                    [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                    [SEVEN, CROWN, BELL, ORANGE, CHERRY],
                ],
                balance=balance,
                bet=bet,
            )
        else:
            return render_template(
                "index.html",
                game=[
                    [SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                    [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                    [SEVEN, CROWN, BELL, ORANGE, CHERRY],
                ],
                bet=0,
            )


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login_error.html", error="Must provide username.")
        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login_error.html", error="Must provide password.")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template(
                "login_error.html", error="Invalid username and/or password."
            )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to game page
        return render_template(
            "game.html",
            game=[
                [SEVEN, CROWN, SEVEN, PLUM, ORANGE],
                [SEVEN, CROWN, SEVEN, SEVEN, STAR],
                [SEVEN, CROWN, BELL, ORANGE, CHERRY],
            ],
            bet=0.0,
        )

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        if password != confirm:
            return render_template(
                "register_error.html", error="Password do not match."
            )
        if len(db.execute("SELECT * FROM users WHERE username = ?", username)):
            return render_template("register_error.html", error="Username exists.")
        else:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                generate_password_hash(password),
            )
            return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()
    return redirect("/")
