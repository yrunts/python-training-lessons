"""Solution to task 1 from lesson 4."""

import sys


def main():
    """Script entry point."""
    file_name = sys.argv[1] if len(sys.argv) > 1 else ''
    if file_name:
        f = open(file_name, 'w')
        f.write(u'Hello world')
        f.close()


if __name__ == '__main__':
    main()

