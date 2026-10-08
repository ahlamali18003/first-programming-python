def ask_question(question_text, options, correct_answer):
    """Show one question and return True if the user's answer is correct."""
    print("\n" + question_text)

    # Display each answer choice with a letter.
    for index, option in enumerate(options):
        print(chr(65 + index) + ". " + option)

    # Keep asking until the user enters a valid answer letter.
    valid_answers = [chr(65 + index) for index in range(len(options))]
    answer = input("Your answer: ").strip().upper()
    while answer not in valid_answers:
        print("Please enter one of these letters:", ", ".join(valid_answers))
        answer = input("Your answer: ").strip().upper()

    # Compare the user's answer with the correct answer.
    if answer == correct_answer:
        print("Correct!")
        return True

    print("Not quite. The correct answer is", correct_answer + ".")
    return False


def run_quiz(questions):
    """Ask every question and return the number the user answered correctly."""
    score = 0

    # The loop repeats once for every question in the quiz.
    for question in questions:
        if ask_question(
            question["question"],
            question["options"],
            question["answer"],
        ):
            score += 1

    return score


def show_result(name, score, total_questions):
    """Display the user's final score and a short result message."""
    print("\n" + name + ", you scored", str(score), "out of", str(total_questions) + ".")

    # Use the score to choose a message for the user.
    if score == total_questions:
        print("Perfect score! Great job!")
    else:
        print("Thanks for playing. Keep practicing!")


# Store each question, its choices, and its correct answer in a list of dictionaries.
quiz_questions = [
    {
        "question": "What is the capital of Kenya?",
        "options": ["Mombasa", "Nairobi", "Kisumu", "Nakuru"],
        "answer": "B",
    },
    {
        "question": "How many sides does a triangle have?",
        "options": ["Two", "Three", "Four", "Five"],
        "answer": "B",
    },
    {
        "question": "Which animal is known as the king of the jungle?",
        "options": ["Elephant", "Giraffe", "Lion", "Zebra"],
        "answer": "C",
    },
]


# Ask for the player's name, run the quiz, and show the final result.
if __name__ == "__main__":
    player_name = input("What is your name? ").strip()
    if not player_name:
        player_name = "Player"

    final_score = run_quiz(quiz_questions)
    show_result(player_name, final_score, len(quiz_questions))