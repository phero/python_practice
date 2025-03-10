def is_leap(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0


def get_days(year, month):
    if month == 2 and is_leap(year):
        return 29

    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month]


def counting_sundays():
    day_of_week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

    count = 0

    # 1901/1/1 is a tuesday
    current_day = 2
    for year in range(1901, 2001):
        for month in range(1, 13):
            if current_day == 0:
                count = count + 1

            days = get_days(year, month)
            # print(month, day_of_week[current_day], days)
            remain = days % 7
            current_day = (current_day + remain) % 7
        print(year, day_of_week[current_day])

    print(count, current_day)


if __name__ == "__main__":
    counting_sundays()
