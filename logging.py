import getopt
import os
import sys
import ntpath

PROGRAM = '\logging.py'

def main():
    if len(sys.argv) < 2:
        print('usage: logging.py <list of directories>')
        sys.exit(2)
    argv = sys.argv[1:]
    for val in argv:
        if not(os.path.isdir(val)):
            print(f'{val} is not a valid directory!')
            continue
        head, tail = ntpath.split(val)
        if tail == "":
            tail = ntpath.basename(head)
        os.chdir(val)
        os.system(f'git --no-pager log -p --pretty=%n%n«%h»¦«%s»¦«%aN»¦«%aD» --reverse -- {val}{PROGRAM} > log{tail}.txt')
        os.system(f'gitk {val}{PROGRAM}')
    print("Done!")

if __name__ == '__main__':
    main()
