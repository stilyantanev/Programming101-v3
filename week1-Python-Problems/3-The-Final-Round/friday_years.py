import datetime


def friday_years(start, end):
    counter_for_fridays = 0
    friday_years = 0

    delta = datetime.timedelta(days=1)
    current_year = start

    start_date = datetime.date(start, 1, 1)
    end_date = datetime.date(end, 12, 31)

    while start_date <= end_date:
        if current_year < start_date.year:
            if counter_for_fridays == 53:
                friday_years += 1

            counter_for_fridays = 0
            current_year += 1

        if start_date.weekday() == 4:
            counter_for_fridays += 1

        start_date += delta

    return friday_years


def main():
    print(friday_years(1000, 2000))
    print(friday_years(1753, 2000))
    print(friday_years(1990, 2015))

if __name__ == '__main__':
    main()
