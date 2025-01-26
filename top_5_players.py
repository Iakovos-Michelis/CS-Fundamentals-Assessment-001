def top_5_users():
    try:
        with open("user_scores.txt", "r") as user_file:
            user_scores = [line.strip().split(",") for line in user_file]
            user_scores = [(s[0], s[1], int(s[2])) for s in user_scores]
            user_scores.sort(key=lambda x: x[2], reverse=True)  # Sort by user_score descending

        print("Top 5 User Scores:")
        for i, (username, datetime_str, user_score) in enumerate(user_scores[:5], start=1):
            print(f"{i}. {username} - Score: {user_score}, Date: {datetime_str}")

    except FileNotFoundError:
        print("User score file not found.")

if __name__ == "__main__":
    top_5_users()
