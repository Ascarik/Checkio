def checkio(text, word):
    text = text.lower().replace(" ", "")
    word = word.lower()

    array_symbols = []
    index = 0
    for line in text.split("\n"):
        if word in line:
            index_word = line.find(word) + 1
            return [index + 1, index_word, index + 1, index_word + len(word) - 1]
        array_symbols.append(line)
        index += 1

    for index, symbol in enumerate(array_symbols):
        if word[0] in symbol:
            top = word[0]
            down = word[0]
            i = 1
            column = 0
            flag = False
            while i < len(word):
                if not flag:
                    column = symbol.find(word[0], column if i == 1 else column + 1)
                    top = word[0]
                    down = word[0]
                    i = 1
                if column == -1 or i >= len(word):
                    break

                if index - i >= 0 and array_symbols[index - i][column] == word[i]:
                    top += word[i]
                    if top == word:
                        return [index + 1, column + 1, index + i + 1, column + 1]
                    else:
                        flag = True
                elif index + i < len(array_symbols) and array_symbols[index + i][column] == word[i]:
                    down += word[i]
                    if down == word:
                        return [index + 1, column + 1, index + i + 1, column + 1]
                    else:
                        flag = True
                else:
                    flag = False

                i += 1

    return [None, None, None, None]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
    And dreaming often, dear,
    I dreamed that, if I counted all,
    -How many would appear?""", "ten") == [2, 14, 2, 16]

    assert checkio("""sdfsfat,
sdfsfae,
sdfsfan,
-How many would appear?""", "ten") == [1, 7, 3, 7]

    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    assert checkio("""Hiall!
Andallgoodbye!
Ofcoursegoodbye.
ornot""", "HAOo") == [1, 1, 4, 1]
print("Coding complete? Click 'Check' to earn cool rewards!")
