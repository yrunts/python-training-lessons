"""Solution to task 6 from lesson 4."""

import sys
import datetime
import shutil
import os


def main():
    """Script entry point."""
    file_name = sys.argv[1] if len(sys.argv) > 1 else ''
    if file_name:
        # copy file
        copy = file_name + "~"
        shutil.move(file_name, copy)
        destination = open(file_name, 'w')
        source = open(copy, 'r')

        # get first line and modify it
        first_line = source.readline()
        new_line = '{:50s}{}\n'.format(str(datetime.datetime.now()),
                                       first_line[50:-1])
        destination.write(new_line)

        # copy all the rest data
        for line in source:
            destination.write(line)

        destination.close()
        source.close()
        os.remove(copy)


def main2():
    file_name = sys.argv[1] if len(sys.argv) > 1 else ''
    if file_name:
        try:
            f = open(file_name, 'r+')
            f.write('{:50s}'.format(str(datetime.datetime.now())))
        except Exception, e:
            raise e


if __name__ == '__main__':
    main2()

