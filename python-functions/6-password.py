def validate_password(password):
    # specialchar = ["$", "@", "#", "%"] this is a list of special characters
    if len(password) < 8:
        return False
    if not any(i.isupper() for i in password):
        return False
    if not any(i.islower() for i in password):
        return False
    if not any(i.isdigit() for i in password):
        return False
    # if not any(i in specialchar for i in password): this is to check if the password contains at least one of the special characters
    # return False
    if any(i in " " for i in password):
        return False
    else:
        return True
    return True


print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
