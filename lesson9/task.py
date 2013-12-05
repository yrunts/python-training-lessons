"""Solution to tasks from lesson 9."""

import sys
import os
import time

def file_copy(source, destination):
    """Copies file content from source file to destination.

    :Parameters:
        - `source`: a `string` source file path;
        - `destination`: a `string` destination file path;
    """
    try:
        source_f = open(source)
    except (OSError, IOError) as e:
        sys.stderr.write('{}\n'.format(e))
    else:
        if os.path.isfile(destination):
            sys.stderr.write('destination file already exists\n')
        else:
            with open(destination, 'w') as f:
                f.write(source_f.read())
        source_f.close()


def advanced_file_copy(source, destination):
    """Copies file content from source file to destination line by line.

    :Parameters:
        - `source`: a `string` source file path;
        - `destination`: a `string` destination file path;
    """
    try:
        source_f = open(source)
    except (OSError, IOError) as e:
        sys.stderr.write('{}\n'.format(e))
    else:
        if os.path.isfile(destination):
            sys.stderr.write('destination file already exists\n')
        else:
            with open(destination, 'w') as f:
                sys.stdout.write('Copying a file "{}" into "{}"\n'.format(
                        source, destination))
                try:
                    for line in source_f:
                        f.write(line)
                        sys.stderr.write('.')
                        time.sleep(1)
                except KeyboardInterrupt:
                    sys.stdout.write('\nOperation terminated by user')
                else:
                    sys.stdout.write('\nOperation complete\n')
                finally:
                    source_f.close()


def main():
    file_copy('1', '2')
    file_copy('alice.txt', '2')
    file_copy('alice.txt', '3')
    advanced_file_copy('alice.txt', '4')

if __name__ == '__main__':
    main()
