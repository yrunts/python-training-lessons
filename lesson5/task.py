"""Solution to task 6 from lesson 4."""

import shutil
import re


def remove_empty_lines(source, destination):
    """Remove empty lines from file by loading fully it to memory.

    :Parameters:
        - `source`: a `string` source file name;
        - `destination`: a `string` file name to store changed text;
    """
    _copy(source, destination)
    f = open(source)
    regexp = re.compile(r'^$\n', re.MULTILINE)
    content, count = re.subn(regexp, '', f.read())
    f.close()
    f = open(destination, 'w')
    print '%s\n' % str(count)
    f.write(content)
    f.close()


def remove_empty_lines_iter(source, destination):
    """Remove empty lines from file using line by line interaction.

    :Parameters:
        - `source`: a `string` source file name;
        - `destination`: a `string` file name to store changed text;
    """
    _copy(source, destination)
    source_file = open(source)
    destination_file = open(destination, 'w')
    count = 0
    regexp = re.compile(r'^$')
    for l in source_file:
        if regexp.match(l):
            count += 1
        else:
            destination_file.write(l)

    print '%s' % str(count)
    source_file.close()
    destination_file.close()


def replace(source, destination, match_pattern, new_value):
    """Replaces lines matching pattern.

    :Parameters:
        - `source`: a `string` source file name;
        - `destination`: a `string` file name to store changed text;
        - `match_pattern`: a `string` with regexp;
        - `new_value`: a `string` value that replaces mathed pattern line;
    """
    _copy(source, destination)
    source_file = open(source)
    destination_file = open(destination, 'w')
    count = 0
    regexp = re.compile(match_pattern)
    for l in source_file:
        if regexp.match(l):
            count += 1
            destination_file.write(new_value)
        else:
            destination_file.write(l)

    print '%s' % str(count)
    source_file.close()
    destination_file.close()


def remove_white_spaces(source, destination):
    """Removes all leading and trailing white-spaces.

    :Parameters:
        - `source`: a `string` source file name;
        - `destination`: a `string` file name to store changed text;
    """
    _copy(source, destination)
    source_file = open(source)
    destination_file = open(destination, 'w')
    count = 0
    patterns = (re.compile(r'^( +)\w*'), re.compile(r'\w*( +)$'))
    for l in source_file:
        for p in patterns:
            l, n = p.subn('', l)
            if n:
                count += 1
        destination_file.write(l)

    print '%s' % str(count)
    source_file.close()
    destination_file.close()


def get_match_count(source, regexp, stop_after = 0):
    """Calculates pattern matches count in file.

    :Parameters:
        - `source`: a `string` source file name;
        - `regexp`: a `regexp` regexp to match;
        - 'stop_after': an `int` signalize to stop iteration afer reaching
                        lines count;

    :Returns:
        - `int` matches count;
    """
    match_count = 0
    with open(source) as f:
        for i, line in enumerate(f):
            if stop_after and i == stop_after:
                break;
            match_count += len(regexp.findall(line))

    return match_count


def advanced_double(source):
    """Calculates double characters occurences, tripples are not counted.
    :Parameters:
        - `source`: a `string` source file name;

    :Returns:
        - `int` matches count;
    """
    match_count = 0
    regexp = re.compile(r'([a-z])\1+', re.I)
    with open(source) as f:
        for line in f:
            for match in regexp.finditer(line):
                if len(match.group()) == 2:
                    match_count += 1

    return match_count


def replace_text(source, destination, old, new):
    """Replaces all occurences of old text to new.

    :Parameters:
        - `source`: a `string` source file name;
        - `destination`: a `string` file name to store changed text;
        - `old`: a `string` with text to replace;
        - `new`: a `string` new replaced text value;

    :Returns:
        - `int` replacement count;
    """
    _copy(source, destination)
    source_file = open(source)
    destination_file = open(destination, 'w')
    words = re.split(r'\W+', old)
    basic_pattern = re.compile(old, re.I)
    words_patterns = []
    for i in range(0, len(words) - 1):
        words_patterns.append({
            'end': re.compile(' '.join(words[0:i+1]) + '$', re.I), 
            'start': re.compile('^' + ' '.join(words[i+1:]))
        })

    match_count = 0
    previous_line = None
    word_end_pattern = None
    for l in source_file:
        # replace if previous line matches end and current matches start
        if word_end_pattern and word_pattern['start'].match(l):
            previous_line = word_end_pattern['end'].sub(new, previous_line)
            l = word_end_pattern['start'].sub('', l)
            match_count += 1

        if previous_line:
            destination_file.write(previous_line)

        # replace inline occurencies
        l, count = basic_pattern.subn(new, l)
        match_count += count

        # find occurencies on line end
        word_end_pattern = None
        for word_pattern in words_patterns:
            if word_pattern['end'].search(l):
                word_end_pattern = word_pattern
                break

        previous_line = l
    destination_file.write(previous_line)

    return match_count 


def _copy(source, destination):
    """Copy file with new name.

    :Parameters:
        - `f`: a `file` to copy;
        - new_name: a `string` copy file name;

    :Returns:
        - `file` file copy with new name;
    """
    shutil.copyfile(source, destination)


def main():
    """Script entry point."""
    remove_empty_lines_iter('alice.txt', 'alice01.txt')
    # remove blank lines
    replace('alice.txt', 'alice02.txt', r'^ +$', '')
    remove_white_spaces('alice.txt', 'alice03.txt')

    vowel_regexp = re.compile(r'[aeiouy]', re.I)
    print 'Vowel letters count: %s' % get_match_count('alice.txt',
                                                        vowel_regexp, 100)

    numbers_regexp = re.compile(r'\b\d+\b')
    print 'Numbers count: %s' % get_match_count('alice.txt', numbers_regexp)

    doubles_regexp = re.compile(r'([a-z])\1+', re.I)
    print 'Number of doubles: %s' % get_match_count('alice.txt',
                                                     doubles_regexp)

    print 'Numbers of doubles without tripples: %s' % advanced_double(
            'alice.txt')

    sentences_regexp = re.compile(r'\.{1,3}')
    print 'Number of sentences: %s' % get_match_count('alice.txt',
                                                       sentences_regexp)

    words_regexp = re.compile(r'(?!\b\d+\b)\b[\w\']+\b')
    print 'Number of words: %s' % get_match_count('alice.txt', words_regexp)

    print 'Replace time: %s' % replace_text('alice.txt', 'alice10.txt',
                                            'Alice was', 'Alice is')


if __name__ == '__main__':
    main()

