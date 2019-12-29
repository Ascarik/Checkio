def checkio(number: int) -> int:

    str_number = str(number)
    result = 1

    for num in str_number:
        if num.isnumeric() and num != "0":
            result*=int(num)

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")