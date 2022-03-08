import getopt
import os
import sys
import ntpath

PROGRAM = '\logging.py'

def main():
    argv = sys.argv[1:]
    try:
        arguments, values = getopt.getopt(argv, 'd:')
    except getopt.error:
        print("Can't parse the arguments\nusage: logging.py -d <list of directories>")
        sys.exit(2)
    if len(arguments) == 0:
        print("usage: logging.py -d <list of directories>")
        sys.exit(2)
    for arg, val in arguments:
        head, tail = ntpath.split(val)
        if tail == "":
            tail = ntpath.basename(head)
        os.chdir(val)
        os.system(f'git --no-pager log -p --pretty=%h»¦«%s»¦«%aN»¦«%aD --reverse -- {val}{PROGRAM} > log{tail}.txt')
        os.system(f'gitk {val}{PROGRAM}')
    print("Done!")

if __name__ == '__main__':
    main()
