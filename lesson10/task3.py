"""Solution to task 2 from lesson 10."""


import sys
import contextlib
import timeit


class Memento(object):
    """Memento as class implementation."""
    def __init__(self, obj, attr, val):
        self.obj = obj
        self.attr = attr
        self.val = val

    def __enter__(self):
        self.old_val = getattr(self.obj, self.attr, None)
        setattr(self.obj, self.attr, self.val)
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback):
        setattr(self.obj, self.attr, self.old_val)


@contextlib.contextmanager
def memento(obj, attr, val):
    """Memento as function with implementation."""
    old_val = getattr(obj, attr)
    setattr(obj, attr, val)
    yield
    setattr(obj, attr, old_val)


def test1():
    with Memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        print sys.exit(1)


def test2():
    with Memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        print sys.exit(1)


def main():
    t1 = timeit.Timer(test1)
    time1 = t1.timeit(number=10000)

    t2 = timeit.Timer(test2)
    time2 = t2.timeit(number=10000)

    print time1
    print time2


if __name__ == '__main__':
    main()
