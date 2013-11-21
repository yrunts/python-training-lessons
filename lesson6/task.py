"""Solution to tasks from lesson 5."""


import timeit
import collections
import re


def concat(s, chars_count=10):
    """Forms string form first and last n-chars of input.

    :Parameters:
        - `s`: a `string`;
        - `chars_count`: an `int` chars count to use in concatination;

    :Returns:
        - `string` concatenated string;
    """
    if len(s) > 2 * chars_count:
        return tuple(s[:chars_count] + s[-chars_count:])
    else:
        return tuple(s)


def test_perfomance():
    """Prints time for instantiated 1000000 list types."""
    print timeit.timeit('tuple(range(0, 10))', number=1000000)
    print timeit.timeit('list(range(0, 10))', number=1000000)
    print timeit.timeit('set(range(0, 10))', number=1000000)


def characters_count(source):
    """Prints a number of times that each English character is used in file.

    :Parameters:
        - `source`: a `string` path to file;
    """
    letter_match = re.compile(r'[a-z]', re.IGNORECASE)
    d = collections.defaultdict(int)
    with open(source) as f:
        for l in f:
            for letter in letter_match.findall(l):
                d[letter.lower()] += 1
    print d

def wc(source):
    """Returns words, lines and characters count for file.

    :Parameters:
        - `source`: a `string` path to file;

    :Retunrs:
        - `tuple` of words, lines and characters count;
    """
    l_count = 0
    w_count = 0
    c_count = 0
    words_pattern = re.compile(r'\b[\w\']+\b')
    with open(source) as f:
        for l in f:
            l_count += 1
            c_count += len(l)
            w_count += len(words_pattern.findall(l))

    return (l_count, w_count, c_count)


def main():
    print 'String: %s, concatenated: %s' % ('some string',
                                            concat('some string'))
    print 'String: %s, concatenated: %s' % (
        'some string some string some striasdfasdf dasf sadf sdf sdd',
         concat('some string some string some striasdfasdf dasf sadf sdf sdd'))

    test_perfomance()
    characters_count('alice.txt')
    print 'Statistis: %s' % str(wc('alice.txt'))
    words = re.findall(r'\b[\w\']+\b', open('alice.txt').read().lower())
    print 'Unique words: %s' % len(set(words))
    print 'Most common: %s' % collections.Counter(words).most_common(20)


if __name__ == '__main__':
    main()
