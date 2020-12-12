def yaml(a):
    # your code here
    result = {}
    list_values = a.split("\n")
    for value in list_values:
        if not value:
            continue
        key, value = value.split(":")
        key, value = key.strip(), value.strip()
        if value.isnumeric():
            value = int(value)
        result[key] = value
    return result


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert {'name': 'Alex', 'age': 12} == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
