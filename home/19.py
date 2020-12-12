def date_time(data: str) -> str:
    # replace this for solution
    date, time = data.split()
    day, month, year = date.split(".")
    hour, minute = time.split(":")

    months = {"01": "January", "02": "February", "03": "March", "04": "April",
              "05": "May", "06": "June", "07": "July", "08": "August",
              "09": "September", "10": "October", "11": "November", "12": "December"}

    day = int(day)
    hour = int(hour)
    minute = int(minute)

    if hour == 1:
        hour = f"{hour} hour"
    else:
        hour = f"{hour} hours"
    if minute == 1:
        minute = f"{minute} minute"
    else:
        minute = f"{minute} minutes"

    return f"{day} {months[month]} {year} year {hour} {minute}"


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
