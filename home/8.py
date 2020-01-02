# На сервере некорректно отрабатывает

def time_converter(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    meridiem = "a.m." if hour < 12 else "p.m."

    if hour == 24:
        hour = 0
    elif hour > 12:
        hour = hour - 12

    if hour == 0 and minutes == "00":
        hour = 12

    return "{0}:{1} {2}".format(int(hour), minutes, meridiem)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('12:00') == '12:00 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
