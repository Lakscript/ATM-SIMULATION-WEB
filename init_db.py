import sqlite3

def init():
    con = sqlite3.connect("atm.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS accounts(
                    token INTEGER PRIMARY KEY,
                    pin INTEGER NOT NULL,
                    balance INTEGER NOT NULL
                );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS history(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token INTEGER,
                    amount INTEGER,
                    action TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );""")
    con.commit()
    con.close()
    print("Database initialized (atm.db)")

if __name__ == "__main__":
    init()