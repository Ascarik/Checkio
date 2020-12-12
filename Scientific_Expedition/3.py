# Taken from mission YAML. Simple Dict

def yaml(a):
    # your code here
    result = {}
    list_values = a.split("\n")
    for value in list_values:
        if not value:
            continue
        key, value = value.split(":")
        key, value = key.strip(), value.strip()
        value = value[1:-1] if value and value[0] == "\"" \
                               and value[-1] == "\"" and value != "\"null\"" else value
        value = value.replace("\\", "")

        if value.isnumeric():
            value = int(value)
        elif value in ["false", "true"]:
            value = True if value == "true" else False
        elif not value or value == "null":
            value = None
        elif value == '"null"':
            value = 'null'
        result[key] = value
    return result


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    print(yaml('name: "Alex Fox"\n'
               'age: 12\n'
               '\n'
               'class: 12b'))
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    print(yaml('name: "Alex \\"Fox\\""\n'
               'age: 12\n'
               '\n'
               'class: 12b'))
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
