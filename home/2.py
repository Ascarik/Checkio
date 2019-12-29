def checkio(text: str) -> str:
    result = dict()
    for ch in text:
        ch = ch.lower()
        if "a" <= ch <= "z":
            if not result.get(ch):
                result.setdefault(ch, 1)
            else:
                result[ch] = result[ch] + 1

    max_element = None

    for element in result.items():
        if max_element == None:
            max_element = element
        else:
            if max_element[1] < element[1]:
                max_element = element
                continue

            if max_element[0] >= element[0] and max_element[1] == element[1]:
                max_element = element

    return max_element[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
