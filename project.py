def check_password_strength(password):
    if len(password) < 8:
        return "Weak (too short)"
    elif any(char.isupper() for char in password) and \
         any(char.islower() for char in password) and \
         any(char.isdigit() for char in password):
        return "Strong"
    else:
        return "Weak"

# Get user input
user_password = input("Enter a password: ")

# Check password strength
password_strength = check_password_strength(user_password)
print("Password strength:", password_strength)
