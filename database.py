import json

DATABASE_FILE = "books.json"

def load_books():
    with open(DATABASE_FILE, "r") as file:
        data = json.load(file)
    return data["books"]

def save_books(books):
    with open(DATABASE_FILE, "w") as file:
        json.dump({"books": books}, file, indent=4)