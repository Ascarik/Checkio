def missing_number(items: list[int]) -> int:
    # your code here
    items.sort()
    lmin = items[1] - items[0]
    if (rmin := items[-1] - items[-2]) < lmin:
        lmin = rmin

    result = 0

    for i in range(len(items)):
        if lmin + items[i] not in items:
            result = lmin + items[i]
            break

    return result


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
