# ATM-SIMULATION-WEB

This project is a **simple ATM simulation system** built using **Python** and connected to a **SQLite database**, with a basic web interface created with **Flask**.

The project includes all essential ATM features such as account creation, login, deposit, withdrawal, and transaction history.

---

## 📌 **About the Project**

This project started as a **Python console-based ATM program**, which I fully developed.
Later, using **Flask and HTML/CSS**, I created a web interface to make it more interactive.
I am not very experienced in web development, so **the UI and frontend structure were created with the help of AI**, while **all the Python logic and database workflow were implemented by me**.

---

## ⭐ **Features**

### ✔ Core ATM Functions (Python authored by me)

* Create new account (auto Token & PIN generation)
* Secure login with Token + PIN
* Deposit money
* Withdraw money with limits
* Transaction history stored with timestamp
* Balance updates in real time
* SQLite database backend

### ✔ Web Interface (UI designed with AI assistance)

* Login page
* Dashboard
* Deposit & Withdraw forms
* History page
* Responsive modern UI (HTML + CSS)

---

## 🗂 **Tech Stack**

| Component | Technology        |
| --------- | ----------------- |
| Backend   | Python, Flask     |
| Database  | SQLite (`atm.db`) |
| Frontend  | HTML, CSS         |
| Tools     | VS Code           |

---

## 📦 Folder Structure

```
project/
│── app.py
│── init_db.py
│── atm.db
│── README.md
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── create_account.html
│   ├── history.html
│
└── static/
    └── css/
        └── style.css
```

---

## ▶️ **How to Run This Project Locally**

Anyone can clone/download this project and run it on their own computer.

### **1. Install Python**

Make sure Python 3.10+ is installed.

### **2. Create a Virtual Environment**

```
python -m venv venv
```

Activate it:

**Windows PowerShell**

```
venv\Scripts\Activate
```

### **3. Install required packages**

```
pip install flask
```

### **4. Initialize the database**

```
python init_db.py
```

This creates the `atm.db` file with required tables.

### **5. Run the application**

```
python app.py
```

### **6. Open in browser**

Go to:

```
http://127.0.0.1:5000
```

---

## 📘 Project Purpose (For College Submission)

This project was built for the **VITyarthi – Build Your Own Project** assignment.
It demonstrates:

* Application of Python logic
* Working with files and databases (SQLite)
* Backend implementation
* Basic frontend integration
* A complete deployed workflow on local system

---

## ✍️ My Contribution

* I **fully developed the Python logic**, database operations, ATM workflow, and backend functionality.
* I am not very experienced in web development, so the **HTML/CSS UI and page styling were created with AI assistance**.
* I integrated everything into a working Flask application.

---

## 📄 License

This project is for academic/learning purposes. Free to modify.

---



