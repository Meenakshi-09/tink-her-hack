import random

genres = ["Romance", "Drama", "Fantasy", "Crime", "Thriller", "Historical", "Old Literature", "Adventure", "Comedy"]
books_by_genre = {
    "Romance": ["Book A", "Book B", "Book C", "Book D", "Book E"],
    "Drama": ["Book F", "Book G", "Book H", "Book I", "Book J"],
}

def roll_dice():
    roll = random.randint(1, 9)
    genre = genres[roll - 1]
    return genre, books_by_genre.get(genre, [])