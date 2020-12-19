def checkio(line1: str, line2: str) -> str:
    # your code here

    words = list(set(line1.split(",")) & set(line2.split(",")))
    words.sort()
    result = ""
    for word in words:
        if result:
            result += f",{word}"
        else:
            result = word
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
                   'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
