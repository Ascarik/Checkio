def sun_angle(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    if (hour >= 18 and minutes != 0) or hour < 6:
        return "I don't see the sun!"
    else:
        degree_minute = 180 / (12 * 60)
        degree_hour = 180 / 12
        hour -= 6
        return hour * degree_hour + minutes * degree_minute


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
