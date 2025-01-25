# quiz.py

def personality_quiz(form_data):
    """Processes the quiz responses and determines a personality-based book recommendation."""

    # Count the number of responses for each personality type
    personality_scores = {
        "adventurous": 0,
        "analytical": 0,
        "romantic": 0,
        "mysterious": 0
    }

    # Increment scores based on user's selections
    for key, value in form_data.items():
        if value in personality_scores:
            personality_scores[value] += 1

    # Determine the dominant personality trait
    dominant_trait = max(personality_scores, key=personality_scores.get)

    # Book recommendations based on personality
    book_recommendations = {
        "adventurous": ["The Hobbit - J.R.R. Tolkien", "Treasure Island - Robert Louis Stevenson"],
        "analytical": ["Sapiens - Yuval Noah Harari", "Thinking, Fast and Slow - Daniel Kahneman"],
        "romantic": ["Pride and Prejudice - Jane Austen", "Me Before You - Jojo Moyes"],
        "mysterious": ["Sherlock Holmes - Arthur Conan Doyle", "Gone Girl - Gillian Flynn"]
    }

    return book_recommendations.get(dominant_trait, ["No recommendations found."])
