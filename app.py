from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "replace-with-a-random-secret"

# -------------------------
# Database connection
# -------------------------
def get_db():
    return sqlite3.connect("atm.db")


# -------------------------
# Home (Login Page)
# -------------------------
@app.route("/")
def home():
    return render_template("login.html")


# -------------------------
# Login POST
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    token = request.form.get("token")
    pin = request.form.get("pin")

    if not token or not pin:
        flash("Please enter token and PIN")
        return redirect(url_for("home"))

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT token FROM accounts WHERE token=? AND pin=?", (token, pin))
    user = cur.fetchone()
    con.close()

    if user:
        return redirect(url_for("dashboard", token=token))
    else:
        flash("Invalid token or PIN")
        return redirect(url_for("home"))


# -------------------------
# Dashboard
# -------------------------
@app.route("/dashboard/<token>")
def dashboard(token):
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT balance FROM accounts WHERE token=?", (token,))
    row = cur.fetchone()
    con.close()

    balance = row[0] if row else 0
    return render_template("dashboard.html", token=token, balance=balance)


# -------------------------
# Create Account (GET + POST)
# -------------------------
@app.route("/create", methods=["GET", "POST"])
def create_account():
    if request.method == "GET":
        return render_template("create_account.html")

    initial = int(request.form.get("initial", 0))

    token = random.randint(10000, 99999)
    pin = random.randint(100, 999)

    con = get_db()
    cur = con.cursor()
    cur.execute("INSERT INTO accounts(token, pin, balance) VALUES(?,?,?)",
                (token, pin, initial))
    con.commit()
    con.close()

    flash(f"Account created! Token: {token}, PIN: {pin}")
    return redirect(url_for("home"))


# -------------------------
# Deposit
# -------------------------
@app.route("/deposit", methods=["POST"])
def deposit():
    token = request.form.get("token")
    amount = int(request.form.get("amount", 0))

    con = get_db()
    cur = con.cursor()

    # Update balance
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE token=?", (amount, token))

    # Insert into history
    cur.execute("INSERT INTO history(token, amount, action) VALUES(?,?,?)",
                (token, amount, "DEPOSIT"))

    con.commit()
    con.close()

    flash("Deposit successful")
    return redirect(url_for("dashboard", token=token))


# -------------------------
# Withdraw
# -------------------------
@app.route("/withdraw", methods=["POST"])
def withdraw():
    token = request.form.get("token")
    amount = int(request.form.get("amount", 0))

    con = get_db()
    cur = con.cursor()

    # Check balance
    cur.execute("SELECT balance FROM accounts WHERE token=?", (token,))
    row = cur.fetchone()

    if not row:
        flash("Account not found")
        con.close()
        return redirect(url_for("home"))

    balance = row[0]

    if amount > balance:
        flash("Insufficient balance")
    elif amount > 20000:
        flash("Cannot withdraw more than 20000 at once")
    else:
        # Deduct and record transaction
        cur.execute("UPDATE accounts SET balance = balance - ? WHERE token=?", (amount, token))
        cur.execute("INSERT INTO history(token, amount, action) VALUES(?,?,?)",
                    (token, amount, "WITHDRAW"))

        con.commit()   # <--- IMPORTANT FIX

        flash("Withdrawal successful")

    con.close()
    return redirect(url_for("dashboard", token=token))


# -------------------------
# Transaction History
# -------------------------
@app.route("/history/<token>")
def history(token):
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        SELECT amount, action, timestamp 
        FROM history 
        WHERE token=? 
        ORDER BY timestamp DESC
    """, (token,))
    rows = cur.fetchall()
    con.close()

    return render_template("history.html", token=token, rows=rows)


# -------------------------
# Start App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)