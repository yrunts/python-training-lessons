"""Solution to task 2 from lesson 4."""

import sys


def main():
    """Script entry point."""
    name = sys.argv[1] if len(sys.argv) > 1 else ''
    if name:
        sys.stdout.write('Hello %s' % name)


if __name__ == '__main__':
    main()

