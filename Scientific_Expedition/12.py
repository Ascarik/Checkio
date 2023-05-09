def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    # your code here
    result = {}
    for v in data:
        if v[0] == "" or v[1] == 0:
            continue
        elif v[0] not in result:
            result[v[0]] = v[1]
        else:
            if result[v[0]] + v[1] == 0:
                del result[v[0]]
            else:
                result[v[0]] = result[v[0]] + v[1]
    return result


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

# These "asserts" are used for self-checking
assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}
assert conv_aggr([('a', 0), ('b', 0), ('', 35)]) == {}

print("The mission is done! Click 'Check Solution' to earn rewards!")
