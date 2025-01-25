from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from dice_game import roll_dice
from quiz import personality_quiz
from database import db, User, Book
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

# Initialize Database
def init_db():
    with app.app_context():
        db.create_all()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        genres = ",".join(request.form.getlist("genres"))

        new_user = User(name=name, email=email, password=password, genres=genres)
        db.session.add(new_user)
        db.session.commit()

        session['user_name'] = name
        session['email'] = email
        return redirect(url_for('dashboard'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if "user_name" not in session:
        return redirect(url_for("register"))

    user = User.query.filter_by(email=session["email"]).first()
    user_genres = user.genres.split(",")

    recommended_books = {
        "romance": ["Pride and Prejudice", "The Notebook"],
        "drama": ["A Thousand Splendid Suns", "To Kill a Mockingbird"],
        "fantasy": ["Harry Potter", "The Hobbit"]
    }

    user_recommendations = [book for genre in user_genres for book in recommended_books.get(genre, [])]

    return render_template("dashboard.html", user_name=session["user_name"], recommended_books=user_recommendations)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        user_answers = request.form
        recommended_books = personality_quiz(user_answers)
        return render_template("quiz_result.html", books=recommended_books)

    return render_template("quiz.html")

@app.route('/quiz_result', methods=['POST'])
def quiz_result():
    """Process quiz answers and return book recommendations."""
    user_answers = request.form.to_dict()
    recommended_books = personality_quiz(user_answers)
    return render_template("quiz_result.html", books=recommended_books)



@app.route('/roll-dice')
def roll():
    genre, books = roll_dice()
    return render_template('dice_result.html', genre=genre, books=books)

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("index"))

@app.route("/mothers")
def mothers():
    return render_template('mother.html')

@app.route("/professional")
def professional():
    return render_template('professional.html')

@app.route("/young")
def young():
    return render_template('young.html')

@app.route("/forum/mothers")
def forum_mothers():
    """Forum for Mothers"""
    return render_template("mothers/forum.html")

@app.route("/forum/professional")
def forum_professional_women():
    """Forum for Professional Women"""
    return render_template("professional/forum.html")

@app.route("/forum/young")
def forum_young():
    """Forum for Young Adult"""
    return render_template("young/forum.html")

if __name__ == '_main_':
    app.run(debug=True)