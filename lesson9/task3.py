"""Solution to task3 from lesson 9."""

import signal
import sys


def alarm(time=1):
    """Scheduled SIGALRM signal."""
    signal.alarm(time)


def alarm_handler(signum, frame):
    """Handles SIGALRM signal."""
    sys.stdout.write('.')
    alarm()


def exit_handler(signum, frame):
    sys.stdout.write('.')
    sys.exit(1)


def main():
    """Script entrance point."""
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.signal(signal.SIGINT, exit_handler)
    alarm()

    while True:
        print raw_input('Enter a message: ')



if __name__ == '__main__':
    main()
