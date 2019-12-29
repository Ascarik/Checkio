def long_repeat(line: str):
    max_element = 0
    cur_element = line[0] if len(line)>0 else ""
    count = 0
    for s in line:
        if cur_element == "":
            cur_element = s
        elif cur_element == s:
            count += 1
        else:
            cur_element = s
            if count > max_element:
                max_element = count
            count = 1

    if count > max_element:
        max_element = count

    return max_element


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('aa') == 2, "Fouth"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
