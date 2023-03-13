#!/usr/bin/env python3


def do_twice(f, a):
    f(a)
    f(a)


def print_twice(txt):
    print(txt)
    print(txt)


def do_four(f, a):
    do_twice(f, a)
    do_twice(f, a)


# do_twice(print_twice,"spam")
do_four(print_twice, "spam")
