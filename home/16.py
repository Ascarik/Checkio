VOWELS = "aeiouy"


def translate(phrase):
    count = 1
    result = ""
    for i, x in enumerate(phrase):
        if x in VOWELS:
            if count == 3:
                count = 1
            elif i + 1 < len(phrase) and x == phrase[i + 1]:
                count += 1
                if count == 3:
                    result += x
        else:
            result += x
            count = 1
    return result


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
