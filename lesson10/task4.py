"""Solution to task 4 from lesson 10."""


def dict_with_attrs(*args):
    """Return class extended from dict with predefined attributes."""
    class CustomDict(dict):
        __slots__ = args

        def __init__(self, *args, **kwargs):
            super(CustomDict, self).__init__(*args)

            for k, v in kwargs.iteritems():
                setattr(self, k, v)

    return CustomDict


def dict_with_attrs2(*args):
    """Returns class with predefined attributes that's behaves like dict."""
    class CustomDict(object):
        __slots__ = args
        __dict__ = {}

        def __init__(self, *args, **kwargs):
            super(CustomDict, self).__init__()
            if args:
                self.__dict__.update(*args)

            for k, v in kwargs.iteritems():
                setattr(self, k, v)

        def __getitem__(self, key):
            return self.__dict__[key]

        def __setitem__(self, key, val):
            self.__dict__[key] = val

        def __delitem__(self, key):
            del self.__dict__[key]

        def __getattr__(self, name):
            return self.__dict__[name]

    return CustomDict


def main():
    Test = dict_with_attrs('test', 'other')
    d = Test({'a': 1}, test='test')
    print d['a']
    print d.test
    d.other = 'Hey!'
    d[10] = 11
    print d[10]

    # # This shall fails:
    d.unknown = 42


if __name__ == '__main__':
    main()
