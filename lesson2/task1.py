"""Solution to taks 1 from lesson 2."""

def factorial(n):
    """Calculates and prints number's factorial.

    :Parameters:
        - `n`: an `int` number to calculate factorial for;
    """
    result = 1
    if n != 0:
        i = n
        while i > 1:
            result *= i
            i -= 1
    print 'Factorial for %s is equal to %s' % (n, result)


def my_args(*args):
    """Prints function arguments.

    :Parameters:
        - `args`: arguments to print;
    """
    print 'My args are %s' % (', '.join([str(a) for a in args]))


def harmony(*args):
    """Calculates and prints numbers harmonic medium value.

    :Parameters:
        - `args`: float numbers to calculate harmonic medium value;
    """
    sum = 0
    for n in args:
        sum += 1.0 / n

    print 'Harmonic medium value is equal to %s' % str(len(args) / sum)


def main():
    factorial(10)
    factorial(2)
    factorial(0)
    factorial(5)
    my_args(1, 2, 3, 5)
    my_args(22, 'asd', 11)
    harmony(1, 2, 4)
    harmony(20, 30, 100, 22, 2)


if __name__ == '__main__':
    main()

