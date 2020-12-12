def backward_string_by_word(text: str) -> str:
    # your code here
    if not text:
        return text
    reverse = text.split(" ")

    result = ""
    for i, st in enumerate(reverse):
        if not st:
            result += " "
        else:
            result += st[::-1]
            if i + 1 < len(reverse):
                result += " "
    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
