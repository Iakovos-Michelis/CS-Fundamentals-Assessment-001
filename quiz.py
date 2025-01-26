import random
import requests

users_file = "users.txt"
scores_file = "scores.txt"
questions_url = "https://opentdb.com/api.php?amount=5&type=multiple"

#Loading users
def load_users():
    try: return dict(line.strip().split(",") for line in open(users_file))
    except: return {}

#Saving users
def save_user(username, password):
    with open(users_file, "a") as f: f.write(f"{username},{password}\n")

#Logging in user
def login():
    users = load_users()
    while True:
        choice = input("1. Login\n2. Register\nChoose: ")
        username = input("Username: ")
        if choice == "1" and users.get(username) == input("Password: "): return username
        if choice == "2" and username not in users:
            save_user(username, input("Password: "))
            return username
        print("Invalid credentials or username exists.")


def fetch_questions():
    try:
        return requests.get(questions_url).json()["results"]
    except: print("Error fetching questions."); return []

#Playing the quiz
def play_game(username):
    questions = fetch_questions()
    if not questions: return
    score = 0
    answers = []  
    correct_answers = [] 

    for i, q in enumerate(questions, 1):
        correct = q["correct_answer"]
        options = random.sample([correct] + q["incorrect_answers"], 4)
        print(f"\nQ{i}: {q['question']}")
        for j, opt in enumerate(options, 1): print(f"{j}. {opt}")

        # Get the user's answer (1-4) and check if it's correct
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if options[answer] == correct:
                score += 1
            answers.append(options[answer])
            correct_answers.append(correct)
        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 4.")
            answers.append(None)
            correct_answers.append(correct)

    # Displaying results
    print(f"\nYour score: {score}/5")
    print("\nQuestion Review:")
    for i, (user_ans, correct_ans) in enumerate(zip(answers, correct_answers), 1):
        print(f"Q{i}: {questions[i-1]['question']}")
        print(f"Your answer: {user_ans if user_ans else 'No answer'}")
        print(f"Correct answer: {correct_ans}")
    
    # Saving score to file
    with open(scores_file, "a") as f: f.write(f"{username},{score}\n")

if __name__ == "__main__":
    username = login()
    while True:
        play_game(username)
        if input("Play again? (yes/no): ").lower() != "yes": break