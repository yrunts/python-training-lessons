"""Solution to task 2 from lesson 2."""


import math
import datetime

class MyNumberPrinter(object):
    """Number printer. Performs print operation with numbers.

    :IVariables:
        - `n`: an `int` number;
        - `time_formats`: accepeted time formats values;
    """
    time_formats = ('s', 'm', 'h', 'd')

    def __init__(self, n):
        super(MyNumberPrinter, self).__init__()
        self.n = n

    def me(self):
        """Prints current number."""
        print 'Number is %s' % str(self.n)

    def factorial(self):
        """Prints current number factorial."""
        print 'Factorial for %s is equal to %s' % (self.n,
                                                   math.factorial(self.n))

    def string(self, s):
        """Prints a string concatenated with itself current number times.

        :Parameters:
            - `s`: an `string`;
        """
        print s * self.n

    def update(self, n):
        self.n = n
        self.me()

    def time_in_past(self, format):
        """Prints past time from now based on delta format.

        :Parameters:
            - `format`: an `string` time delta format;
        """
        if format in self.time_formats:
            delta = self.n
            if format == 'm':
                delta *= 60
            elif format == 'h':
                delta *= 60 * 60
            elif format == 'd':
                 delta *= 60 * 60 * 24
            past = datetime.datetime.now() - datetime.timedelta(seconds=delta)
            print 'time is %s' % past


def main():
    a = MyNumberPrinter(10)
    a.me()
    a.factorial()
    a.string('a1')
    a.update(5)
    a.factorial()
    a.string('a1')
    a.time_in_past('s')
    a.time_in_past('m')
    a.time_in_past('h')
    a.time_in_past('d')

if __name__ == '__main__':
    main()

