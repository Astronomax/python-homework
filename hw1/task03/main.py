import os
import sys


stdin_fname = '-'

def compute_number_width(files):
    global stdin_fname
    width = 1
    minimum_width = 1
    regular_total = 0
    for f_name in files:
        if f_name == stdin_fname:
            minimum_width = 7
        else:
            regular_total += os.stat(f_name).st_size
    while 10 <= regular_total:
        regular_total /= 10
        width += 1
    if width < minimum_width:
        width = minimum_width
    return width

def write_counts(lines, words, bytes, f_name):
    global number_width
    print("%*d" % tuple([number_width, lines]), end="")
    print(" %*d" % tuple([number_width, words]), end="")
    print(" %*d" % tuple([number_width, bytes]), end="")
    print(f" {f_name}")

def process_file(f):
    content = f.read()
    lines = len(content.split("\n")) - 1
    words = len(content.split())
    bytes = len(content)
    return lines, words, bytes

files = sys.argv[1:]
if len(files) == 0:
    number_width = compute_number_width(["-"])
    lines, words, bytes = process_file(sys.stdin)
    write_counts(lines, words, bytes, "")
else:
    lines_total = 0
    words_total = 0
    bytes_total = 0

    number_width = compute_number_width(files)
    for f_name in files:
        if f_name == stdin_fname:
            lines, words, bytes = process_file(sys.stdin)
        else:
            with open(f_name) as f:
                lines, words, bytes = process_file(f)
        write_counts(lines, words, bytes, f_name)
        lines_total += lines
        words_total += words
        bytes_total += bytes
    if len(files) > 1:
        write_counts(lines_total, words_total, bytes_total, "total")