"""
Scans the currently connected network
and writes data concerning the signal strength
to a logfile

Created by adam on 2/13/18
"""
__author__ = 'adam'


import subprocess
import time
import argparse
import datetime

LOGFILE_NAME = 'wifi-log.txt'
TIMEOUT_INTERVAL_IN_SECONDS = 5


def getTimestampString():
    """Returns the standard string format of timestamp used in making a file name"""
    # return datetime.date.isoformat(datetime.now())
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")


def write_to_log(data):
    with open(LOGFILE_NAME, 'a') as f:
        d = "%s %s" % (getTimestampString(), data)
        print(d)
        f.write(d)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
    parser.add_argument(dest='interface', nargs='?', default='wlan0',
                        help='wlan interface (default: wlan0)')
    args = parser.parse_args()

    print('\n---Press CTRL+Z or CTRL+C to stop.---\n')

    while True:
        cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,
                               stdout=subprocess.PIPE)
        for line in cmd.stdout:
            if 'Link Quality' in line:
                write_to_log(line.lstrip(' '))
            elif 'Not-Associated' in line:
                write_to_log('No signal')
        time.sleep(TIMEOUT_INTERVAL_IN_SECONDS)