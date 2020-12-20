def caps_lock(text: str) -> str:
    # your code here
    result = ""
    flag = False
    for index, ch in enumerate(text):
        if flag:
            if ch != 'a' and ch != 'A':
                result += ch.upper()
                continue
            else:
                flag = False
                continue
        if ch != 'a' and ch != 'A' or index == 0:
            result += ch
        else:
            flag = True
    return result


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
