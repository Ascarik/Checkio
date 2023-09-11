from typing import Callable, Any


def checkio(time_string: str) -> str:
    # your code here
    bin2: Callable[[Any], str] = lambda x: "{0:02b}".format(x)
    bin3: Callable[[Any], str] = lambda x: "{0:03b}".format(x)
    bin4: Callable[[Any], str] = lambda x: "{0:04b}".format(x)

    morse: Callable[[Any], str] = lambda x: x.replace("0", ".").replace("1", "-")
    numbers = time_string.split(":")

    result = ""
    for i, number in enumerate(numbers):
        num = int(number)
        first = num // 10
        second = num % 10
        if i == 0:
            first = morse(bin2(first))
            second = morse(bin4(second))
            result += "{0} {1}".format(first, second)
        else:
            first = morse(bin3(first))
            second = morse(bin4(second))
            result += " : {0} {1}".format(first, second)

    return result


print("Example:")
print(checkio("10:37:49"))

# These "asserts" are used for self-checking
assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"
assert checkio("0:10:2") == ".. .... : ..- .... : ... ..-."

print("The mission is done! Click 'Check Solution' to earn rewards!")
