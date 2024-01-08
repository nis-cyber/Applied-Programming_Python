import re

class SSTS:
    @staticmethod
    def validate_password(password):
        # Define the regular expressions for each rule
        regex_length = r'^.{6,16}$'
        regex_lowercase = r'[a-z]'
        regex_uppercase = r'[A-Z]'
        regex_digit = r'[0-9]'
        regex_special_char = r'[$#@]'

        # Check if the password meets all the rules
        if (re.search(regex_length, password) and
                re.search(regex_uppercase, password) and
                re.search(regex_digit, password) and
                re.search(regex_special_char, password)):
            return True
        else:
            return False


# Example usage
password1 = "Password123#"
password2 = "WeakP@ss"

# Validate passwords
print("Password1 is valid:", SSTS.validate_password(password1))
print("Password2 is valid:", SSTS.validate_password(password2))
