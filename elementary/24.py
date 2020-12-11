def split_pairs(a):
    # your code here
    if not a:
        return []
    if len(a) % 2 != 0:
        a += "_"

    i = 0
    result = []
    while True:
        result.append(a[i:i + 2])
        i += 2
        if i >= len(a):
            break
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
