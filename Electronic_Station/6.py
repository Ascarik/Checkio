# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        return False

    if password.lower().count("password") > 0:
        return False

    symbols = set(password)
    numbers = sum(c.isdigit() for c in symbols)
    letters = sum(c.isalpha() for c in symbols)

    if len(password) <= 9 and numbers == 0:
        return False

    if len(password) <= 9 and letters == 0:
        return False

    if len(password) > 9 and (letters >= 3 or numbers >= 3):
        return True

    return letters >= 1 and numbers >= 1 and (letters + numbers) >= 3


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False
