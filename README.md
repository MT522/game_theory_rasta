# Rasta Game Theory Event Website

Welcome to the official Django-based web platform for the **Rasta Game Theory** event! This project provides an interactive web interface for participants to log in, view their group's current scores, and track leaderboard standings.

---

## 🧠 Features

- 🏠 **Homepage** with event branding and basic info  
- 🔐 **User Authentication** (register, login, logout)  
- 🏆 **Group Rankings** page displaying scores and standings  
- 🎯 Modular design for scalability  

---

## 🛠 Tech Stack

- Python 3.11+  
- Django 4.x  
- SQLite (default, easy development)  
- Bootstrap 5 (for styling)  

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rasta-game-theory.git
cd rasta-game-theory

### 2. Set up a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

```bash
pip install -r requirements.txt

### 4. Apply migrations

```bash
python manage.py migrate

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser

### 6. Run the development server

```bash
python manage.py runserver

Now visit http://127.0.0.1:8000 to view the site.
