"""Solution to tasks from lesson 8."""


import types
import contextlib
from functools import wraps, partial

# global transactions counter
t_count = 0

def transaction_manager(func):
    """Decorator """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global t_count
        t_count += 1
        print 'Transaction %s for %s started' % (t_count, func.__name__)
        try:
            func(*args, **kwargs)
        except Exception, e:
            print 'Transaction %s for %s cancelled' % (t_count, func.__name__)
        else:
            print 'Transaction %s for %s completed' % (t_count, func.__name__)
    return wrapper


@transaction_manager
def example1():
    """Test function for transaction_manager."""
    print 'example 1'


@transaction_manager
def example2():
    """Test function for transaction_manager."""
    raise Exception()


@transaction_manager
def example3(text):
    """Test function for transaction_manager."""
    print text


def print_decorator(text):
    """Decorator prints input text after function call."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print text
        return wrapper
    return decorator


@print_decorator('World')
def example4(arg):
    """Test function for print_decorator decorator."""
    print arg


@contextlib.contextmanager
def transaction(status):
    """Transaction implementation using contextmanager decorator."""
    global t_count
    t_count += 1
    count = t_count
    print 'Transaction %s started' % count
    try:
        yield
    except Exception, e:
        print 'Transaction %s cancelled' % count
    else:
        print 'Transaction %s completed' % count


def my_func(a, b, c):
    """Test function using transaction function."""
    with transaction('root'):
        print a
        with transaction('nested successful'):
            print b
        with transaction('nested with error'):
            print c
            raise Exception


def template_methods(template, method_table):
    def decorator(cls):
        for k, v in method_table.iteritems():
            method = partial(template, **v)
            setattr(cls, k, types.MethodType(method, cls))
        return cls
    return decorator


def template(self, a, b, c):
    print self.x, a, b, c

method_table = {
    'test': dict(a=10, c=20),
    'other_test': dict(b=30),
}

@template_methods(template, method_table)
class A(object):
    x = 10


def main():
    example1()
    example2()
    example3('Hi')
    example4('Hello')

    my_func(1, 2, 3)

    a = A()
    a.test(b=2)
    a.other_test(a=2, c=2)


if __name__ == '__main__':
    main()
