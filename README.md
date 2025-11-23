# ATM Simulation Web App

A simple and functional *ATM Simulator* built using *Python (Flask)* and *SQLite*.  
The project allows users to:

- Create a new ATM account  
- Login using Token + PIN  
- Deposit money  
- Withdraw money  
- View transaction history  

### 🔧 Technologies Used
- *Python Flask* – backend logic (written completely by me)
- *SQLite* – local database storage
- *HTML (Jinja Templates)* – page structure & routing
- *CSS* – UI styling  
  (basic CSS written by me, enhanced with small assistance from AI)

---

## 🚀 Features
- Account creation with *auto-generated Token & PIN*
- Deposit and withdrawal with instant balance update
- Withdrawal limits & balance validation
- Transaction history recording (DEPOSIT/WITHDRAW)
- Clean UI with simple navigation
- Fully working local Flask web application

---

## 📌 How to Run This Project (Local Setup)

Follow these steps to run the ATM Simulator on your laptop.

### *1. Clone the repository*
bash
git clone https://github.com/Lakscript/ATM-SIMULATION-WEB.git

2. Navigate to the project directory

cd ATM-SIMULATION-WEB

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

5. Install dependencies

pip install flask

(Only Flask is required because SQLite is built-in.)


---

🗄️ Database

The repository already contains:

atm.db — main database

init_db.py — script to initialize database tables (only needed if db is deleted)


If you ever want to recreate the database:

python init_db.py


---

▶️ Run the Application

python app.py

You should see:

Running on http://127.0.0.1:5000/

Open the link in your browser.


---

📂 Project Structure

ATM-SIMULATION-WEB/
│── app.py
│── atm.db
│── init_db.py
│── data.csv
│── /templates
│     ├── login.html
│     ├── create_account.html
│     ├── dashboard.html
│     ├── history.html
│     └── layout.html
│── /static/css
│     └── style.css


---

👨‍💻 Developer Information

This project is fully written by Lakshit Batra,
studying B.Tech CSE.

All backend logic (Flask, Python, SQLite, routing, HTML templates) is written completely by me.

I used AI only to refine the CSS styling and improve the UI visually.



---

📄 License

This project is open for educational use.
