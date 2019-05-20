#!/usr/bin/env python3
import calendar as cal     # Note the use of "import as"


def main():
    cal.setfirstweekday(cal.SUNDAY)
    lists = (list(cal.day_name), list(cal.day_abbr),
             list(cal.month_name), list(cal.month_abbr))
    for aList in lists:
        print(aList)

    result = cal.month(2016, 1)  # Calendar for January 2016
    print(result)

    cal.prmonth(2017, 3, w=5)  # Calendar for March 2017


if __name__ == "__main__":
    main()
