import getopt
import os
import sys

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
        #print(f"arg: {arg}, val: {val}")
        os.chdir(val)
        os.system('git --no-pager log > log.txt')

if __name__ == '__main__':
    main()
