"""
Scans all connected networks
and writes data concerning the signal strength
to a logfile


An entry reported by iwlist scan looks like this:
  Cell 01 - Address: 98:DE:D0:7D:4B:3F
                    ESSID:"CarriageHouse"
                    Protocol:IEEE 802.11bgn
                    Mode:Master
                    Frequency:2.462 GHz (Channel 11)
                    Encryption key:on
                    Bit Rates:144 Mb/s
                    Extra:rsn_ie=30140100000fac040100000fac040100000fac020c00
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: Unknown: DD850050F204104A0001101044000102103B00
                     Quality=100/100  Signal level=78/100


"""
__author__ = 'adam'

import subprocess
import time
import datetime

# Where we are writing to
LOGFILE_NAME = 'all-wifi-log.txt'

# How long to wait between sampling
TIMEOUT_INTERVAL_IN_SECONDS = 5

# The string which will allow us to easily see where an entry starts
ENTRY_START = '***** \n'


def getTimestampString():
    """Returns the standard string format of timestamp used in making a file name"""
    # return datetime.date.isoformat(datetime.now())
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")


def write_to_log(data):
    with open(LOGFILE_NAME, 'a') as f:
        d = "%s %s \n %s" % (ENTRY_START, getTimestampString(), data)
        print("%s Sample taken. Written to log" % getTimestampString())
        f.write(d)
        f.close()


if __name__ == '__main__':
    print('\n---Press CTRL+Z or CTRL+C to stop.---\n')

    while True:
        c = 'iwlist scan'
        cmd = subprocess.Popen(c, shell=True,
                               stdout=subprocess.PIPE)
        out = ''
        for line in cmd.stdout:
            out += line.lstrip(' ')
        write_to_log(out)
        time.sleep(TIMEOUT_INTERVAL_IN_SECONDS)
