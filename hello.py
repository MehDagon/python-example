from __future__ import print_function
import sys

print('tests starting')

def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'worldXD'


def main():
    hello(say_what())
    print('lololo')
    return 0


if __name__ == '__main__':
    sys.exit(main())
