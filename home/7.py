from typing import List


def checkio(game: List[str]) -> str:
    for i in range(0, len(game)):
        vertical = 1
        horizontal = 1
        up_to_down = 1
        down_to_up = 1
        for j in range(1, len(game)):
            # по горизонтали
            if (game[i][j] == game[i][j - 1]) and game[i][j] != '.':
                horizontal += 1
            if horizontal == 3: return game[i][j - 1]

            # по вертикали
            if (game[j][i] == game[j - 1][i]) and game[j - 1][i] != '.':
                vertical += 1
            if vertical == 3: return game[j - 1][i]

            # по вертикали сверху вниз
            if (game[j][j] == game[j - 1][j - 1]) and game[j - 1][j - 1] != '.':
                up_to_down += 1
            if up_to_down == 3: return game[j - 1][j - 1]

            # по вертикали cнизу вверх
            if (game[-j][j - 1] == game[-j - 1][j]) and game[-j - 1][j] != '.':
                down_to_up += 1
            if down_to_up == 3: return game[-j - 1][j]

    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
