import re


def checkio(line: str) -> int:
    # your code here
    gl = ('A', 'E', 'I', 'O', 'U', 'Y')
    sl = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z')
    line = line.upper()
    line = re.sub("[.,!?]", " ", line)
    words = line.split(sep=" ")

    count = 0
    for word in words:
        w1 = [word[i] for i in range(0, len(word), 2)]
        w2 = [word[i] for i in range(1, len(word), 2)]

        if len(w1) > 0 and len(w2) > 0:
            count = method_name(count, gl, sl, w1, w2)
    print(count)
    return count


def method_name(count, gl, sl, w1, w2):
    if all(elem in sl for elem in w1) and all(elem in gl for elem in w2):
        count += 1
    elif all(elem in sl for elem in w2) and all(elem in gl for elem in w1):
        count += 1
    return count


if __name__ == "__main__":
    print("Example:")
    print(checkio("My name is ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio("My name is ...") == 3
    assert checkio("Hello world") == 0
    assert checkio("A quantity of striped words.") == 1
    assert checkio("Dog,cat,mouse,bird.Human.") == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
