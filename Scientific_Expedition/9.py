def follow(instructions):
    # your code here
    x, y = (0, 0)
    for ch in instructions:
        if ch == 'l':
            x -= 1
        elif ch == 'r':
            x += 1
        elif ch == 'f':
            y += 1
        elif ch == 'b':
            y -= 1
    return (x, y)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
