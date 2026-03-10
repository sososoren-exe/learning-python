#CLI Password Manager
import random

import getpass

import json

try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = {}

while True:
    user_prog_password = getpass.getpass("What password would you like to set as the master password for the Password Manager? (case sensitive) ")
    confirm_user_prog_password = getpass.getpass("Confirm password: ")

    if user_prog_password == confirm_user_prog_password:
        print(f"Master password set successfully!")
        break
    else:
        print("Passwords don't match! Not saved. \n")

master_password = user_prog_password
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempt = input("Enter master password to access Password Manager (case sensitive): ")

    if attempt == master_password:
        print("Access granted! \n")
        break

    else:
        attempts = attempts + 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect. {remaining} attempts remaining. \n")
        else:
            print("Incorrect password. Access denied.")
            exit()

while True:
    print("    Password Manager    ")
    print("1. Add a password")
    print("2. View all passwords")
    print("3. Search for a password")
    print("4. Delete a password")
    print("5. Check password strength")
    print("6. Clear all passwords")
    print("7. Generate a random strong password")
    print("8. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        new_site = input("Please input website name: ")
        new_password = getpass.getpass("Please input password (hidden): ")
        confirm_password = getpass.getpass("Confirm password: ")

        if new_password == confirm_password:
            passwords[new_site] = new_password
            with open("passwords.json", "w") as file:
                json.dump(passwords, file)
            print(f"Password for {new_site} added successfully!")
        else:
            print("Passwords don't match! Not saved. \n")
    
    elif choice == "2":
        if passwords:
            print("Here are your saved passwords: ")
            for site, password in passwords.items():
                hidden = "*" * len(password)
                print(f"{site}: {hidden}")
            
            reveal = input("Do you want to reveal this password? (yes/no): ")
            if reveal.lower() == "yes":
                site = input("Which site?:")
                if site in passwords:
                    for attempt_num in range(max_attempts):
                        attempt = input("Enter master password to view password: ")
                        if attempt == master_password:
                            print("Access granted!\n")
                            print(f"{site}: {passwords[site]}\n")
                            break
                        else:
                            remaining = max_attempts - (attempt_num + 1)
                            if remaining > 0:
                                print(f"Incorrect. {remaining} attempts remaining.\n")
                            else:
                                print("Incorrect password. Access denied.\n")
        else:
            print("No passwords saved yet! \n")
    
    elif choice == "3":
        if passwords:
            for key in passwords:
                print(f"{key} \n")
        
            view = input("Here are your saved sites. Which site's password would you like to view? ")

            if view in passwords:
                print("Site exists!")
                for attempt_num in range(max_attempts):
                    attempt = input("Enter master password to view password: ")
                    if attempt == master_password:
                        print("Access granted!\n")
                        print(f"Password for {view}: {passwords[view]}\n")
                        break
                    else:
                        remaining = max_attempts - (attempt_num + 1)
                        if remaining > 0:
                            print(f"Incorrect. {remaining} attempts remaining.\n")
                        else:
                            print("Incorrect password. Access denied.\n")
            else:
                print("No such site found. \n")
        else:
            print("No password saved yet! \n")
    
    elif choice == "4":
        print("Here are you sites with saved passwords: ")
        for key in passwords:
            print(f"{key} \n")
        
        del_pass = input("Which site and password would you like to delete? ")
        option = input("Are you sure you want to delete this password? (Yes/No) ")
        if option.lower() == "yes":
            if del_pass in passwords:
                del passwords[del_pass]
                with open("passwords.json", "w") as file:
                    json.dump(passwords, file)
                print(f"Password for {del_pass} deleted successfully!")
        
            else:
                print("No such password exists. \n")
        else:
            print("Deletion cancelled. \n")
    
    elif choice == "5":
        check_pass = input("Enter password to check: ")
        has_length = len(check_pass) >=8
        has_upper = any(char.isupper() for char in check_pass)
        has_lower = any(char.islower() for char in check_pass)
        has_number = any(char.isdigit() for char in check_pass)
        special = "!@#$%^&*"
        has_special = any(char in special for char in check_pass)
        
        strength = 0
        
        strength = sum([has_length, has_upper, has_lower, has_number, has_special])
        
        if strength == 5:
            print("Strong password! ✅")
        elif strength >= 3:
            print("Medium password. ⚠️") 
        else:
            print("Weak password. ❌")
        
        print(f"Password meets {strength}/5 requirements")

        if not has_length:
            print("- Needs at least 8 characters")
        if not has_upper:
            print("- Needs uppercase letter")
        if not has_lower:
            print("- Needs lowercase letter")
        if not has_number:
            print("- Needs a number")
        if not has_special:
            print("- Needs special character (!@#$%^&*)")
        print("\n")
        
    elif choice == "6":
        clear = input("Are you sure you want to clear all saved passwords? (Yes/No) ")
        if clear.lower() == "yes":
            passwords.clear()
            with open("passwords.json", "w") as file:
                json.dump(passwords, file)
            print("Passwords cleared successfully!")
        else:
            print("Clearing cancelled. \n")
    
    elif choice == "7":
        low_letters = "abcdefghijklmnopqrstuvwxyz"
        upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*"
        all_chars = low_letters + upper_letters + numbers + symbols

        password = ""
        for i in range(12):
            password = password + random.choice(all_chars)
        
        print(f"{password} \n")

    elif choice == "8":
        print("Program Closed.")
        break
