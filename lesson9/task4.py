"""Solution to task4 from lesson 9."""

import signal
import sys
import atexit
import os
import time


UNCATCHED_SIGNALS = [signal.SIGKILL, signal.SIGSTOP]

total_received = 0
total_resets = 0


def get_signals():
    """Returns all signals codes."""
    signals = []
    for n in dir(signal):
        if n.startswith('SIG') and not n.startswith('SIG_'):
            if n:
                signals.append(getattr(signal, n))
    return signals


def signal_handler(signum, frame):
    """Signals handler, calculates received signals cound."""
    global total_received
    total_received += 1


def exit_handler():
    """Exit handler."""
    global total_received
    global total_resets
    sys.stdout.write('Total reseived: {}\n'.format(total_received))
    sys.stdout.write('Total resets: {}\n'.format(total_resets))


def terminate_handler(signum, frame):
    """Signals handler to perform exit."""
    signal_handler(signum, frame)
    sys.exit(1)


def reset_handler(signum, frame):
    """Signals handler to reset counters."""
    signal_handler(signum, frame)
    global total_received
    global total_resets
    sys.stdout.write('Reset: {}\n'.format(total_received))
    total_resets += 1
    total_received = 0


def alarm_handler(signum, frame):
    """Handles SIGALRM signal."""
    sys.stdout.write('.')
    signal.alarm(60)


def main():
    """Script entrance point."""
    atexit.register(exit_handler)

    for s in get_signals():
        if s not in UNCATCHED_SIGNALS:
            signal.signal(s, signal_handler)

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(60)
    signal.signal(signal.SIGINT, terminate_handler)
    signal.signal(signal.SIGTERM, terminate_handler)
    signal.signal(signal.SIGHUP, reset_handler)

    os.kill(os.getpid(), signal.SIGUSR1)
    os.kill(os.getpid(), signal.SIGUSR2)
    os.kill(os.getpid(), signal.SIGEMT)

    os.kill(os.getpid(), signal.SIGHUP)

    os.kill(os.getpid(), signal.SIGUSR1)
    os.kill(os.getpid(), signal.SIGUSR2)

    while True:
        pass


if __name__ == '__main__':
    main()
