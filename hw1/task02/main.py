import sys

stdin_fname = '-'

def tail_file(f, n_lines):
    print(''.join(f.readlines()[-n_lines:]), end="")

files = sys.argv[1:]
if len(files) > 0:
    first_file = True
    print_headers = True if len(files) > 1 else False
    for f_name in files:
        if print_headers:
            pretty_filename = "standard input" if f_name == stdin_fname else f_name
            prefix = "" if first_file else "\n"
            print(f"{prefix}==> {pretty_filename} <==\n", end="")
            first_file = False
        if f_name == stdin_fname:
            tail_file(sys.stdin, 10)
        else:
            with open(f_name) as f:
                tail_file(f, 10)
else:
    tail_file(sys.stdin, 17)