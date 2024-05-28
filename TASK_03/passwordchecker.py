import re

def check_password_strength(password):
    # Define criteria
    length_criteria = 8
    uppercase_criteria = True
    lowercase_criteria = True
    digit_criteria = True
    special_char_criteria = True
    
    # Check length
    if len(password) < length_criteria:
        return "Weak: Password should be at least {} characters long.".format(length_criteria)
    
    # Check uppercase
    if uppercase_criteria and not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    
    # Check lowercase
    if lowercase_criteria and not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    
    # Check digit
    if digit_criteria and not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    
    # Check special character
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if special_char_criteria and not special_chars.search(password):
        return "Weak: Password should contain at least one special character."
    
    return "Strong: Password meets complexity criteria."

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)
