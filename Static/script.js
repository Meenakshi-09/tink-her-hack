// 🎲 Dice Rolling Game for Expert Readers
function rollDice() {
    let result = Math.floor(Math.random() * 9) + 1; // Generates a number between 1 and 9
    let genres = ["Romance", "Drama", "Fantasy", "Crime", "Thriller", "Historical", "Old Literature", "Adventure", "Comedy"];
    let selectedGenre = genres[result - 1];

    alert("You rolled a " + result + "! Your genre is: " + selectedGenre);
    window.location.href = "/recommendations?genre=" + encodeURIComponent(selectedGenre);
}

// 🎯 Quiz Form Validation
function validateQuizForm(event) {
    let selectedOption = document.querySelector('input[name="quiz_option"]:checked');
    if (!selectedOption) {
        alert("Please select an answer before submitting.");
        event.preventDefault(); // Prevent form submission
    }
}

// 📌 Attach validation to quiz forms
document.addEventListener("DOMContentLoaded", function () {
    let quizForm = document.getElementById("quizForm");
    if (quizForm) {
        quizForm.addEventListener("submit", validateQuizForm);
    }

    let diceButton = document.getElementById("rollDiceBtn");
    if (diceButton) {
        diceButton.addEventListener("click", rollDice);
    }
});

