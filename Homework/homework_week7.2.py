import csv

username = input("Username:")
pin = input("PIN:")

user_found = False

try:
    with open('users.csv', mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['Username'] == username and row['Pin'] == pin:
                print(f"Welcome {row['First name']} {row['Last name']}")
                user_found = True
                break
                
        if not user_found:
            print("User not found")

except FileNotFoundError:
    print("The file 'users.csv' was not found.")