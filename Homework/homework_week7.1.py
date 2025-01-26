word = input("Type the word you search for: ")

try:
    with open('story.txt', 'r') as file:
        content = file.read()

        word_counter = content.lower().split().count(word.lower())

    print(f"The word '{word}' appears {word_counter} times in the story.")
except FileNotFoundError:
    print("The file 'story.txt' was not found.")