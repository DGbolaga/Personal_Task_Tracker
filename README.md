
---

# 📝 Personal\_Task\_Tracker

**NitPy Final Project**
A minimal and efficient personal task tracker built with **Flask**, intended to help users manage tasks with ease — from adding and filtering to sorting and updating task statuses.

---

## 🎯 Project Overview

This project was developed as a final project for NitPy. It allows users to:

* Add tasks with descriptions, priorities, and due dates.
* View all tasks with a clean, categorized layout.
* Filter by **status** or **priority**.
* Sort by **due date**, **priority**, or **added date**.
* Mark tasks as done or revert them to pending.
* Delete individual tasks.

This project demonstrates the use of form validation, dynamic filtering/sorting, and secure database operations using Flask and CS50’s SQL abstraction.

---

## 📂 Folder Structure

```
Personal_Task_Tracker/
├── data/               # SQLite database file (auto-generated)
│   └── tasks.db
├── src/                # Core app logic
│   ├── app.py          # Main Flask application
│   ├── create_db.py    # Script to initialize the database
│   ├── forms.py        # Flask-WTF forms
├── static/             # Styles
│   └── styles.css
├── templates/          # HTML templates
│   ├── index.html
│   └── tasks.html
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS (vanilla), Jinja2
* **Database:** SQLite (accessed via CS50 SQL Library)
* **Forms:** Flask-WTF
* **Environment Variables:** python-dotenv

---

## 📌 Why CS50 Library?

I chose to use the [CS50 Python library](https://cs50.readthedocs.io) for handling SQL queries for its:

* **Conciseness** – less boilerplate to write SQL queries.
* **Safety** – built-in protection against SQL injection.
* **Familiarity** – a tool I’m already comfortable working with.

---

## 🔒 Security Note

All user input is properly validated using **Flask-WTF**, and database interactions are protected against SQL injection using **parameterized queries** via CS50’s `db.execute()`.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DGbolaga/Personal_Task_Tracker.git
cd Personal_Task_Tracker
```

### 2. Create & Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with:

```
SECRET_KEY=your_secret_key_here
```

### 5. Initialize the Database

If `data/tasks.db` does not exist, create it by running:

```bash
python src/create_db.py
```

You can safely delete `data/tasks.db` anytime to reset the database. Just re-run the script above.

---

## ▶️ Running the App

```bash
python src/app.py
```

Visit: [http://localhost:5001](http://localhost:5001)

---

## 💡 Example Usage

1. Add a new task from the **Add Task** page.
2. View your tasks under **View All Tasks**.
3. Use **Filter** or **Sort** to organize your list.
4. Click to **toggle status** or **delete** a task.

---

## ✅ Features

* ✅ Add, delete, or mark tasks as done/pending.
* ✅ Task prioritization and due date support.
* ✅ Intuitive sorting & filtering.
* ✅ Dynamic and responsive flash messages.
* ✅ Clean and readable UI built with HTML & CSS.
* ✅ Relevant docstrings added throughout the code for clarity and maintainability.

---

## 🤖 AI Usage Disclosure

Some sections of this project — including this `README`, parts of the code refactoring, and UI/UX copywriting — were enhanced using **AI assistance** (OpenAI's ChatGPT, Claude AI).
All final implementations were reviewed and tested by the project author.

---

## ✍️ Author

**Omogbolaga Daramola**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
