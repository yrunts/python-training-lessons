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
    a_gen = itertools.repeat(a)
    b_gen = itertools.count(b, a)
    c_values = list(itertools.chain.from_iterable(
        itertools.repeat(range(a, c+1) + range(c-1, a, -1), b)))
    c_values.append(a)
    c_gen = itertools.chain.from_iterable(c_values)
    return itertools.izip(a_gen, b_gen, c_values)


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


def consumer(text=None):
    """Returns generator that prints consumed text.

    :Parameters:
        - `text': a `string` text to print;

    :Returns:
        - `generator`;
    """
    while True:
        if text:
            print text
        text = yield text


def tail(filename, n=10):
    """Returns n lines of a file in from end to begining

    :Parameters:
        - `filename': a `string` path to a file;
        - 'n' - an `int` lines count;
    """
    f = open(filename)
    print '\n'.join(list(itertools.islice(tail_generator(f), n)))
    f.close()


def tail_generator(f):
    """Returns generator reading file lines from end to start.

    :Parameters:
        - `f': a `file`;

    :Returns:
        - `generator`;
    """
    f.seek(0, 2)
    blocksize = 1024
    ending = ''
    while f.tell() != 0:
        try:
            f.seek(-blocksize, 1)
        except IOError:
            blocksize = f.tell()
            f.seek(-blocksize, 1)
        block = f.read(blocksize) + ending
        f.seek(-blocksize, 1)
        lines = block.split('\n')
        ending = lines.pop(0)
        while lines:
            yield lines.pop(-1)


def main():
    print factorial(10)
    print factorial(3)
    print factorial(1)
    print factorial(0)

    print multiplier(100)

    gen = fibonacci()
    print list(itertools.islice(gen, 0, 100))
    print list(itertools.islice(gen, 0, 1000, 10))

    print list(super_func(1, 2, 3))

    gen = flatten('ABC', 'DEF', 'GHJKLMN')
    print list(gen)

    c = consumer()
    c.next()
    for line in flatten(itertools.islice(open('alice.txt'), 10),
                        itertools.islice(open('alice.txt'), 10)):
        c.send(line)

    tail('alice.txt', 10)


if __name__ == '__main__':
    main()
