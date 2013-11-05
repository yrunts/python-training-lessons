"""Solution to task 2 from lesson 4."""

import sys
import os
import datetime
import pwd


def main():
    """Script entry point."""
    if len(sys.argv) == 1:
        dir_path = os.getcwd()
    elif len(sys.argv) == 2:
        dir_path = sys.argv[1]
    else:
        sys.stderr.write('ERROR: too much arguments \n')
        return 0

    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            path = os.path.join(dir_path, f)
            stats = os.stat(path)
            mode = stats.st_mode
            print '{} {} {} {} {}'.format(
                datetime.datetime.fromtimestamp(stats.st_mtime),
                pwd.getpwuid(stats.st_uid).pw_name,
                oct(mode & 0777), 
                f, 
                stats.st_size,)
        return 1
    else:
        sys.stderr.write('ERROR: path does not exist \n')
        return 0


if __name__ == '__main__':
    sys.exit(main())

