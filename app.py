import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure app
app = Flask(__name__)

# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("password")
        passwordcf = request.form.get("confirmation")
        if len(username) == 0:
            return apology("Username cannot be blank")
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        if len(rows) != 0:
            return apology("Username already exists")
        if len(password) == 0:
            return apology("Password cannot be blank")
        if password != passwordcf:
            return apology("Passwords do not match")
        hash = generate_password_hash(password, 'pbkdf2', 16)
        new_user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        session["username"] = username
        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/", methods=["GET", "POST"])
@login_required
def main2():
    if request.method == "POST":
        topic = request.form.get("topic")
        print("hhshsh")
        print(topic)
        content = request.form.get("content")
        print(content)
        db.execute("INSERT INTO diaries (username, topic, content) VALUES(?,?,?)", session["username"], topic, content)
        return redirect("/")
    else:
        rows = db.execute("SELECT time, topic, content FROM diaries WHERE username = ?", session["username"])
        return render_template("main.html", rows=rows,name=session["username"])
