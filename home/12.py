def safe_pawns(pawns: set) -> int:
    count = 0
    for sym in pawns:
        if (str(chr(ord(sym[0]) - 1) + str(int(sym[1]) - 1)) in pawns) \
                or (str(chr(ord(sym[0]) + 1) + str(int(sym[1]) - 1)) in pawns):
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
