def checkio(data: str) -> bool:

    if len(data)< 10:
        return False

    result = {1: False, 2:False, 3:False}
    for ch in data:
        if "A" <= ch <= "Z":
            result[1] = True
        elif "a" <= ch <="z":
            result[2] = True
        elif "0" <= ch <="9":
            result[3] = True

    for key in result.keys():
        if not result[key]:
            return False


    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")