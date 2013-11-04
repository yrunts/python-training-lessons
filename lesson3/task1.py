"""Solution to task 1 from lesson 3."""


def test():
    """Prints strings in different representation."""
    print 'It\'s a test python string\nwith a "newline" character.'
    print r'It\'s a test python string\nwith two backslashes an no "newline" ' \
          r'character.'
    print '''It's a test python string
             with a "newline" character and leading white-space.'''
    print "It's a test python string\nwith a \"newline\" character."
    print r"It's a test python string with two \"backslash\" characters."
    print """It's a test python string\nwith a "newline" character."""


def draw_cat():
    """Draws cheshire cat with strings."""
    print '_-_-_-_-_-_-_\n' \
          '\           /\n' \
          '|  ^_____^  |\n' \
          '/  (.) (.)  \\\n' \
          '|  ( t   )  |  Miaowww\n' \
          '\    ==/    /\n' \
          '|           |\n' \
          '\'"\'"\'"\'"\'"\'"\''

    print '''
_-_-_-_-_-_-_
\           /
|  ^_____^  |
/  (.) (.)  \\
|  ( t   )  |  Miaowww
\    ==/    /
|           |
'"'"'"'"'"'"'
'''

    print r'_-_-_-_-_-_-_'
    print r'\           /'
    print r'|  ^_____^  |'
    print r'/  (.) (.)  \\'
    print r'|  ( t   )  |  Miaowww'
    print r'\    ==/    /'
    print r'|           |'
    print '\'"\'"\'"\'"\'"\'"\''

    print """
_-_-_-_-_-_-_
\           /
|  ^_____^  |
/  (.) (.)  \\
|  ( t   )  |  Miaowww
\    ==/    /
|           |
'"'"'"'"'"'"'
"""


def join(*args, **kwargs):
    """Prints all positional and named argumets using string join method."""
    if args:
        print ', '.join([str(s) for s in args])
    if kwargs:
        sub_items = []
        for k, v in kwargs.items():
            sub_items.append(''.join([k, '=', v]))
        print ', '.join(sub_items)


def format(*args, **kwargs):
    """Prints all positional and named argumets using string join and format
       methods.
    """
    if args:
        print ', '.join([str(s) for s in args])
    if kwargs:
        sub_items = []
        for k, v in kwargs.items():
            sub_items.append('{}={}'.format(k, v))
        print ', '.join(sub_items)


def split(s):
    """Restores function arguments from join and format functions.

    :IVariables:
        - `s`: an `string` output from join or format method;
    """
    args_str, kwargs_str = s.split('\n')
    args = tuple(args_str.split(', '))
    kwargs = {}
    for s in kwargs_str.split(', '):
        k, v = s.split('=')
        kwargs[k] = v
    print args
    print kwargs


def get_last_str(s):
    """Returns a last element (separated by a last comma) or the entire string 
       if there is no comma in it.

    :IVariables:
        - `s`: an `string`;
    """
    return s.split(',')[-1] if ',' in s else s


VOWEL_LETTERS = ['a', 'e', 'i', 'o', 'u', 'y']
REPLACED_MAP = dict((l, l.upper()) for l in VOWEL_LETTERS)

def upper_vowel(s):
    """Uppercases all vowel letters in string.

    :IVariables:
        - `s`: an `string`;
    """
    for k, v in REPLACED_MAP.iteritems():
        s = s.replace(k, v)
    return s


def slicing(s):
    """Returns the first 10 characters off string concatenated with the last
       10 characters.

    :IVariables:
        - `s`: an `string`;
    """
    return s[:10] + s[-10:] if len(s) > 10 else s


def main():
    test()
    draw_cat()
    join(111, 'asdf', c='d', onemore='new_value')
    format(111, 'asdf', c='d', onemore='new_value')

    output = '111, asdf\n' \
             'onemore=new_value, c=d'
    split(output)

    print get_last_str('bla bla')
    print get_last_str('bla1,bla2,bla3')
    print get_last_str('1,2,3,4,5,6,7')
    print upper_vowel('sadfgsa dg345 dfg d')
    print slicing('1234567890qwertyuiopasdfghjkl')
    print slicing('123')



if __name__ == '__main__':
    main()
