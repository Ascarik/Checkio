def from_camel_case(name: str) -> str:
    # replace this for solution

    result = ""
    for i, s in enumerate(name):
        if i != 0 and s.isupper():
            result += "_"
        result += s.lower()

    return result


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
