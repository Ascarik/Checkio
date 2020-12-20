from typing import List


def letter_queue(commands: List[str]) -> str:
    # your code here
    stack = ""
    for command in commands:
        if "PUSH" in command:
            stack += command.split()[1]
        else:
            stack = stack if not stack else stack[1:]
    return stack


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
                        'POP',
                        'POP',
                        'PUSH Z',
                        'PUSH D',
                        'PUSH O',
                        'POP',
                        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
                         'POP',
                         'POP',
                         'PUSH Z',
                         'PUSH D',
                         'PUSH O',
                         'POP',
                         'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
