#!/usr/bin/python3
import sys
"""
script for log pasrsing

reads from stdin line by line and computes metrics
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
    Total file size up to that point
    count of read status code up to that point
"""


def stat_info(size, status_codes):
    """
    function to print the file size and status code

    Arguments:
        size - total file size
        status code - the status codes
    """
    print("File size: {}".format(size))

    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


size = 0
count = 0
status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

try:
    for lines in sys.stdin:
        if count != 0 and count % 10 == 0:
            stat_info(size, status_codes)

        lines = lines.split()

        try:
            stat = int(lines[-2])

            if str(stat) in status_codes.keys():
                status_codes[str(stat)] += 1
        except Exception:
            pass

        try:
            size += int(lines[-1])
        except Exception:
            pass

        count += 1

        stat_info(size, status_codes)
except KeyboardInterrupt:
    stat_info(size, status_codes)
    raise
