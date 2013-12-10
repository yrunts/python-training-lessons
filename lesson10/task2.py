"""Solution to task 2 from lesson 10."""


class TruthTable(object):
    def __nonzero__(self):
        if hasattr(self, '__true_values__') and self in self.__true_values__:
            return True
        if hasattr(self, '__false_values__') and self in self.__false_values__:
            return False
        return True


class TrueTest(int, TruthTable):
    __true_values__ = (0, 1, 2, 3)


class FalseTest(str, TruthTable):
    __false_values__ = ('false', hash('no'))


print bool(TrueTest(0)), bool(FalseTest(''))
