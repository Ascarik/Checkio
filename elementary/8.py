def most_frequent(data: list) -> str:

    result = dict()

    for el in data:
        if not result.get(el):
            result.setdefault(el,1)
        else:
            result[el] = result[el] + 1

    result = sorted(result.items(),  key=lambda x: -x[1])

    return result[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')