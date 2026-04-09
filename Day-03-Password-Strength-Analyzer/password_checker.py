import re

def check_password_strength(password):
    
    strength = 0
    
    # Length check
    if len(password) >= 8:
        strength += 1
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    
    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Strength result
    if strength <= 2:
        return "Weak Password"
    elif strength == 3 or strength == 4:
        return "Medium Password"
    else:
        return "Strong Password"


# Take input from user
password = input("Enter password: ")

result = check_password_strength(password)

print("Password Strength:", result)