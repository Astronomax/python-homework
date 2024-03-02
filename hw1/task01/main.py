import sys


stdin_fname = '-'

def process_file(f):
    for line_no, line in enumerate(f):
        print('%6d\t' % tuple([line_no + 1]), end="")
        print(line, end="")

if len(sys.argv) == 1 or sys.argv[1] == stdin_fname:
    process_file(sys.stdin)
else:
    with open(sys.argv[1]) as f:
        process_file(f)
    print("")