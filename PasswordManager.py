import json
from getpass import getpass

# Load Passwords from JSON
def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
        return passwords
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save Password on JSON
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

# Adding new Password
def add_password():
    site = input("\nType the website or service: ")
    username = input("Type your username: ")
    password = getpass("Type your password: ")

    passwords = load_passwords()
    passwords[site] = {'username': username, 'password': password}
    save_passwords(passwords)
    print(f"Password for {site} succesfully added.")

# Recovering Password
def recover_password():
    site = input("Type which website or service you want to recover a password: ")
    passwords = load_passwords()

    if site in passwords:
        username = passwords[site]['username']
        password = passwords[site]['password']
        print(f"\nUsername: {username}")
        print(f"Password: {password}")
    else:
        print(f"Password for {site} not found.")

# Main Menu
while True:
    print("\nPassword Manager\n")
    print("1. Add password")
    print("2. Recover password")
    print("3. Exit")

    choice = input("\nChoose a option (1/2/3): ")

    if choice == '1':
        add_password()
    elif choice == '2':
        recover_password()
    elif choice == '3':
        break
    else:
        print("Invalid Option. Try again.")
