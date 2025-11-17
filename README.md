# ATM-SIMULATION-WEB
ATM Simulation System (Python + Flask + SQLite)

This project is a web-based ATM Simulation System built as part of the VITyarthi “Build Your Own Project” requirement.

The core ATM logic (Python functions, transactions, rules, and validation) was fully developed by me.
For the web interface (HTML/CSS) and SQLite integration, I took guidance and assistance from AI tools to convert my Python CLI project into a proper web application.

📌 Project Overview

This system simulates the basic operations of an ATM:

User login using Token + PIN

Creating new accounts with automatically generated credentials

Deposits

Withdrawals (with rules like max ₹20,000 per transaction)

Transaction history with timestamps

SQLite database integration for storing user data and logs

✨ Features
1. Account Management

Create an account

Auto-generated Token + PIN

Initial deposit

2. ATM Operations

Deposit money

Withdraw money

Check balance

View complete transaction history

3. Backend (My Contribution)

All Python logic (deposit, withdraw, history, login handling)

ATM rules and validations

SQLite table design

Database operations (INSERT, UPDATE, SELECT)

4. Frontend (Assisted Using AI)

Login, dashboard, create-account pages

Modern UI styling using HTML + CSS

Responsive glassmorphism theme

🛠️ Technologies Used

Python 3

Flask (Web Framework)

SQLite3 (Database)

HTML + CSS (User Interface)

📂 Folder Structure
project/
│── app.py
│── init_db.py
│── atm.db
│── README.md
│── static/
│    └── css/style.css
│── templates/
     ├── login.html
     ├── dashboard.html
     ├── history.html
     ├── create_account.html

▶️ How to Run

Activate virtual environment

.\venv\Scripts\activate


Run database initializer

python init_db.py


Start the Flask server

python app.py


Open the browser:

http://127.0.0.1:5000/

📌 Notes

The backend logic was originally written as a Python console ATM project, then expanded into a web app.

UI design and Flask routing structure were improved with AI assistance.

📜 License

This project is created for academic use under VITyarthi project submission.
