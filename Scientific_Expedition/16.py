def to_camel_case(name: str) -> str:
    # replace this for solution
    words = name.split("_")
    result = ""

    for word in words:
        result += word.capitalize()

    return result


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
