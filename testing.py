import unittest
import most_active_cookie
import io
from contextlib import redirect_stdout
import sys


class testCookie(unittest.TestCase):
    def testBasic(self):
        with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/cookie_log.csv', '-d', '2018-12-09'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'AtY0laUfhglK3lC7')

    # Multiple most active cookies
    def testMultipleActive(self):
        with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/cookie_log.csv', '-d', '2018-12-08'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG')

    # No cookie found at given date
    def testNoCookieDate(self):
        with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/cookie_log.csv', '-d', '2018-07-01'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'There is no cookie at this date')

    # Randomly generated set
    def testRandom(self):
        with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/random_cookies.csv', '-d', '2014-07-31'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'OG9IaCZbQ59jSzW7')

    # Large randomly generated set
    def testLarge(self):
        with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/10klarge.csv', '-d', '2025-04-31'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'rIEZh2prh4arbVKW')

    # Missing argument (date)
    def testWrongArgs1(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()) as capture:
            #with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/cookie_log.csv', '-d'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'Incorrect arguments to run program')

    # -d specifier incorrect
    def testWrongArgs2(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()) as capture:
            #with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/cookie_log.csv', '-c', '2018-12-08'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'Please use -d to mark the date')

    # Try on directory
    def testWrongArgs3(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()) as capture:
            #with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/empty', '-d', '2018-12-08'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'The target is not a file')

    # File that isn't a csv
    def testWrongArgs4(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()) as capture:
            #with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/empty.txt', '-d', '2018-12-08'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'This is not a csv file')

    # Column names in csv are incorrect
    def testWrongColumns(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()) as capture:
            #with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/broken1.csv', '-d', '2018-12-08'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'Columns not in cookie log format')

    # Row in csv fails to match cookie/time pattern
    def testWrongFormat(self):
        with self.assertRaises(SystemExit), redirect_stdout(io.StringIO()) as capture:
            #with redirect_stdout(io.StringIO()) as capture:
            most_active_cookie.main(['most_active_cookie', 'testing_files/broken2.csv', '-d', '2018-12-08'])
        capture = capture.getvalue().strip()
        self.assertEqual(capture, 'Contains wrong format of cookie/timestamp')


if __name__ == '__main__':
    unittest.main()