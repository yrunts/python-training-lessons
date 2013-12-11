"""Solution to task 4 from lesson 10."""


from collections import defaultdict

class Proxy(object):
    """Proxy implementation that caclulates object methods calls count."""
    def __init__(self, obj):
        super(Proxy, self).__init__()
        self.__dict__['obj'] = obj
        self.__dict__['counter'] = defaultdict(int)

    def __getattr__(self, name):
        self.__dict__['counter'][name] += 1
        return getattr(self.__dict__['obj'], name)

    def __setattr__(self, name, value):
        setattr(self.__dict__['obj'], name, value)

    def get_counter(self):
        return self.__dict__['counter']


class A(object):

    phrase = 'Test'

    def test(self):
        print self.phrase


def main():
    proxy = Proxy(A())
    type(proxy.test)
    proxy.phrase = 'Hello World!'
    proxy.test()

    print proxy.get_counter()


if __name__ == '__main__':
    main()
