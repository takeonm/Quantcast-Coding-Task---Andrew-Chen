## Quantcast coding task

This command line program takes a cookie log file and returns the most active cookie of a given day.
The command is run by:
./most_active_cookie [filename].csv -d [YYYY-MM-DD]
and will print the most active cookie(s) seen in the log on that date.

The program is written in python and tested with the unittest library.

Test files are located in the testing_files folder, and all tests can be run using:
./testing