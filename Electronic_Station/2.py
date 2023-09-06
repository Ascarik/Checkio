def sort_by_ext(files: list[str]) -> list[str]:
    # your code here
    dot = list()
    nums = list()
    for file in files:
        if file.startswith(".") and file.count(".") == 1:
            dot.append(file)
        else:
            nums.append(file)

    result = sorted(dot) + sorted(nums, key=sort_custom)
    return result


def sort_custom(x: str):
    i = x.rfind(".")
    return x[i:], x[0:i]


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

assert sort_by_ext(['1.cad', '2.bat', '1.aa', '1.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']

print("The mission is done! Click 'Check Solution' to earn rewards!")
