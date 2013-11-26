"""Solution to tasks from lesson 7."""


import itertools
import collections


def factorial(n):
    """Return factorial for number using non-recursive strategy.

    :Parameters:
        - `n`: a `number`;

    :Returns:
        - `number` factorial value for n;
    """
    return 1 if n == 0 else reduce(lambda x, y: x*y, range(1, n+1))


def multiplier(n):
    """Returns int numbers smaller than input that is multipliers of 3 and next
    number (n + 1) is multiplier of 5.

    :Parameters:
        - `n`: a `number`;

    :Returns:
        - `list` with numbers;
    """
    return [x for x in range(1, n + 1) if x % 3 == 0 and (x + 1) % 5 == 0]


def fibonacci():
    """Fibonacci sequence generator.

    :Returns:
        - `generator` for fibonacci sequence;
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def super_func(a, b, c):
    """"Generates output using next conditions:
        - the first number shall be equal to the first function argument;
        - the second number shall start with the second function argument and
        increase by the first function argument after each turn;
        - the third number shall loop between the first and the third argument
        forth and back several times that is equal to the second argument;

    :Returns:
        - `generator`;
    """
    b_prev = b - a
    c_gen = itertools.cycle(itertools.chain(range(a, c + 1), range(c - 1, a, -1)))
    while True:
        yield a, a + b_prev, c_gen.next()
        b_prev += a


def flatten(*args):
    """Returns flatten output for input interables as generator.

    :Parameters:
        - `args': a `list` with interables;

    :Returns:
        - `generator`;
    """
    pending = len(args)
    nexts = itertools.cycle(iter(it).next for it in args)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = itertools.cycle(itertools.islice(nexts, pending))


def consumer(interable):
    """Returns generator for interable input.

    :Parameters:
        - `interable': an `interable`;

    :Returns:
        - `generator`;
    """
    while True:
        yield interable.next()


def tail(filename, n=10):
    """Returns n lines of a file in reversed order

    :Parameters:
        - `filename': an `interable`;
        - 'n' - an `int` lines count;
    """
    print ''.join(open(filename).readlines()[:-n:-1])



def main():
    print factorial(10)
    print factorial(3)
    print factorial(1)
    print factorial(0)

    print multiplier(100)

    gen = fibonacci()
    print list(itertools.islice(gen, 0, 100))
    print list(itertools.islice(gen, 0, 1000, 10))

    gen = super_func(1, 2, 3)
    print list(itertools.islice(gen, 0, 10))

    gen = flatten('ABC', 'DEF', 'GHJKLMN')
    print list(gen)

    gen = consumer(open('alice.txt'))
    gen2 = consumer(open('alice.txt'))
    for l in flatten(itertools.islice(gen, 0, 10), itertools.islice(gen2, 0, 10)):
        print l

    tail('alice.txt', 10)


if __name__ == '__main__':
    main()
