import re

def check_password_strength(password):
  
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

  
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."


    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

 
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."

  
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets the criteria for strength."


password_to_check = input("Enter the password to check: ")
result = check_password_strength(password_to_check)
print(result)
