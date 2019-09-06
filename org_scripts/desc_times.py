#!/usr/bin/env python
""" 
Script to check timezones of DESC collaborators. For
usage:
    ```
    python desc_times.py -h

    Examples:
    ---------
    python desc_times.py --hour 7 --month 9 --year 2019 --day 4 # 7am Sep/4 Project Time (SLAC
    python desc_times.py --hour 16 --month 9 --year 2019 --day 4 --tzinfo 'Europe/Stockholm' # 4pm (16) at Stockholm, Sweden
    # input strings should be members of `pytz.common_timezones`
    ```
R. Biswas (@rbiswas4).
"""
from datetime import datetime
import pytz
from datetime import tzinfo


def desc_time(hour=8, minute=0, day=30, month=7, year=2019, tzinfo=None):
    if tzinfo is None:
        tzinfo='US/Pacific'
    d = datetime(year, month, day, hour, minute)
    dt = pytz.timezone(tzinfo).localize(d)
    collabtzs = tuple(('US/Pacific', 'America/Denver', 'America/Phoenix', 'US/Central',
                       'US/Eastern', 'Europe/Belfast', 'Europe/London',
                       'Europe/Paris', 'Europe/Stockholm', 'Europe/Ljubljana',
                       'Europe/Berlin', 'America/Toronto', 'Africa/Johannesburg'))
    lst = []
    for tz in collabtzs:
        lst.append(":".join(list((tz, dt.astimezone(pytz.timezone(tz)).strftime('%m-%d %H%M')))))
    return '\n'.join(lst)

if __name__=='__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='script for times of DESC SN collaborators')
    parser.add_argument('--tzinfo', default='US/Pacific', help='timezone string')
    parser.add_argument('--hour', type=int, default=8, help='time in hours 0-24')
    parser.add_argument('--minute', type=int, default=0, help='time in mins 0-60')
    parser.add_argument('--month', type=int, default=7, help='month number')
    parser.add_argument('--day', type=int, default=30, help='day')
    parser.add_argument('--year', type=int, default=2019, help='date in year')

    args = parser.parse_args()
    print(args)

    tstamps = desc_time(tzinfo=args.tzinfo, year=args.year, month=args.month,
                         day=args.day, hour=args.hour, minute=args.minute)
    print(tstamps)
