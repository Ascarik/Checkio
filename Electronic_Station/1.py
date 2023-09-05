def words_order(text: str, words: list) -> bool:
    # your code here

    result = True

    t = text.split(sep=" ")
    prev = None
    for word in words:
        if not prev:
            prev = word
        elif prev == word:
            return False
        if word not in t:
            result = False
            break
        else:
            # text = text[text.find(word) + len(word):]
            t = t[t.index(word) + 1:]

    return result


print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
        words_order("hi world world im here hi world world im here", ["world", "here"])
        == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
