# 🎬 Personal Movie Tracker (JSON Powered)

A **simple command-line application in Python** that lets you **track your favorite movies**, including their title, genre, and rating — all stored locally in a JSON file.

---

## 📌 About the Project

This project demonstrates how to use **JSON as a lightweight database** to store and manage data in a structured format. It's a beginner-friendly Python project that covers:

- Reading and writing JSON files
- Handling user input
- Searching data
- Avoiding duplicate entries
- Basic error handling

---

## ⚙️ Features

- ✅ Add new movies (title, genre, rating)
- 📂 View all movies saved
- 🔍 Search movies by title or genre
- 🚫 Prevent duplicate movie entries
- 🗃️ Save movie data persistently in a `.json` file
- 📉 Graceful handling of invalid inputs

---

## 🛠 Technologies Used

- Python 3.x
- `json` module
- `os` module
- CLI (Command Line Interface)

---

## 🧪 Sample Output

```text
Mymoviedb
 1. Add movie
 2. View All movie
 3. Search movie
 4. Exit
choce an option (1-4) : 1
Enter the movie name: Inception
Enter Genre :Sci-Fi
Enter the rating(1-10) :9.5
Movie added

Mymoviedb
 1. Add movie
 2. View All movie
 3. Search movie
 4. Exit
choce an option (1-4) : 2
inception -- sci-fi -- 9.5
