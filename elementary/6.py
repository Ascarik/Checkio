def checkio(str_number: str, radix: int) -> int:
    return covert(str_number, radix)


def covert(str_number: str, radix: int) -> int:
    step = 0
    result = 0
    for i in range(len(str_number) - 1, -1, -1):
        if "A" <= str_number[i].upper() <= "Z":
            if radix <= ord(str_number[i]) - 55: return -1
            result += (ord(str_number[i]) - 55) * pow(radix, step)
        else:
            if radix <= int(str_number[i]): return -1
            result += int(str_number[i]) * pow(radix, step)
        step += 1
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
