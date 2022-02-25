import sys
from pathlib import Path
import re

# Prints the most common cookie(s) of a given date in the cookie hashmap
def mostActiveCookie(cookieMap, date):
    cookies = cookieMap.get(date)
    if cookies == None:
        print('There is no cookie at this date')
        return #not exit because not finding a cookie isn't necessarily an error

    mostTimes = max(cookies.values())
    active = [c for c,t in cookies.items() if t == mostTimes]
    for c in active:
        print(c)

# Splits a line in the csv file to return the cookie code and date
def parseCookie(line):
    # Regex for each part of cookie code, date, and time
    cookie = '[a-zA-Z0-9]{16}'
    date = '[1-2][0-9]{3}-([0][1-9]|1[0-2])-([0-2][1-9]|3[0-1])'
    time = 'T([0-1][0-9]|2[0-3])(:[0-5][0-9]){2}\+00:00'
    check = re.search('^' + cookie + ',' + date + time + '$', line)
    if not check:
        print('Contains wrong format of cookie/timestamp')
        exit(1)

    check = check.group()
    # Return the cookie and date
    return check[0:16], check[17:27]

def main(argv):
    # Argument Checking
    try:
        assert len(argv) == 4, 'Incorrect arguments to run program'
        assert argv[2] == '-d', 'Please use -d to mark the date'
        assert Path(argv[1]).is_file(), 'The target is not a file'
        assert argv[1][-4:] == '.csv', 'This is not a csv file'
    except AssertionError as error:
        print(error)
        exit(1)

    cookieMap = {}
    # Keep track of cookies by date and occurence in hashmap
    with open(argv[1], 'r') as file:
        try:
            assert file.readline().rstrip() == 'cookie,timestamp', 'Columns not in cookie log format'
        except AssertionError as error:
            print(error)
            exit(1)

        for line in file:
            cookie, day = parseCookie(line)
            if cookieMap.get(day) == None:
                cookieMap[day] = {}
            cookieMap[day][cookie] = cookieMap[day].get(cookie, 0) + 1
        # Print the most active cookie
        mostActiveCookie(cookieMap, argv[3])


if __name__ == '__main__':
    main(sys.argv)