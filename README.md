# Crown Fiesta

Crown Fiesta is a slot game built with Flask and Bootstrap. It has 5 reels and 9 paylines, and features colorful graphics.

## Installation

To install Crown Fiesta, you need to have Python 3 and pip installed on your system. Then, follow these steps:

- Clone this repository or download the zip file.
- Navigate to the project directory and create a virtual environment with `python -m venv venv`.
- Activate the virtual environment with `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux/MacOS.
- Install the required dependencies with `pip install -r requirements.txt`.
- Run the app with `flask run`.

## Usage

To play Crown Fiesta, open your browser and go to `http://localhost:5000`. You will see the game interface with the reels, the paytable, and the buttons. You can adjust your bet size. To spin the reels you must first register, log in, click the `Spin` button.

The game has various symbols, such as crowns, 7s, bells, cherries, grapes, lemons and more. The crown symbol is the wild, which can substitute for any other symbol except the scatter. The scatter symbol is the dollar and the star.


## Files

- `app.py` contains the routing logic.
- `helpers.py` contains the functions needed to calculate the winnings
- `symbols.py` represents the class of symbols

## Database

I have used SQLite in combination with the cs50 library to facilitate working with databases.
- `crown.db` is the database containing the following tables:
```
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    bet NUMERIC NOT NULL DEFAULT 5.0,
    balance NUMERIC NOT NULL DEFAULT 1000.00
    );

CREATE TABLE transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    bet NUMERIC NOT NULL,
    win NUMERIC NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```
- `reset.sql` is the file used to reset the database

### Requirements
- `Flask` - for flask framework
- `cs50` - for SQL database handling
- `Flask-Session` - for session handling
- `pytz` - for hashing passwords
- `requests` - for handling requests

## Paytable

![Paytable](/static/paytable.png)


## Attributions

- Inspired by EGT's Shining Crown game
- <a class="link-dark" href="https://www.flaticon.com/free-icons/crown" title="crown icons">Crown icons created by ultimatearm - Flaticon</a>
