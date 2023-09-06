# Taken from mission Acceptable Password I
import re


def is_acceptable_password(password: str) -> bool:
    if (len(password) <= 6):
        return False
    else:
        return bool(re.search(r"[a-zA-Z]{1,}", password)) and bool(re.search(r"[0-9]{1,}", password))


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password('1234567') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
