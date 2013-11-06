"""Solution to task 2 from lesson 5."""

import sys
import os


def main():
    """Script entry point."""
    print 'Python executable: {}'.format(sys.executable)
    print 'Current module: {}'.format(__file__)
    print 'Command line arguments: {}'.format(sys.argv)
    print 'Imported module names: {}'.format(sys.modules)
    print 'Environment variables: {}'.format(os.environ)


if __name__ == '__main__':
    main()

