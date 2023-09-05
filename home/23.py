def changing_direction(elements: list[int]) -> int:
    # your code here
    count = 0
    if len(elements) > 1:
        down, up = up_down(elements)

        flag = None

        if up:
            flag = True
        elif down:
            flag = False

        value = None
        for i, v in enumerate(elements):

            if value is None:
                value = v
                continue

            if flag:
                if v >= value:
                    pass
                else:
                    count += 1
                    flag = not flag
                value = v
                continue

            else:
                if v <= value:
                    pass
                else:
                    count += 1
                    flag = not flag
                value = v
                continue

        return count

    return count


def up_down(elements):
    down = None
    up = None
    temp = elements[0]
    for e in elements[1:]:
        if temp < e:
            up = True
            break
        elif temp > e:
            down = True
            break
    return down, up


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
