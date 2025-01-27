import random

def generate_password(length=10):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print("Your random password is:", generate_password())