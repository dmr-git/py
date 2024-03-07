#!/usr/bin/env python3

# Filename:     drutils_tst.py
# Author:       DMR

import sys


def main():
    """
    This is the main function.  It will be used to call the various examples.
    """
    from drutils import get_date
    from drutils import min_max

    bday = get_date()
    print(bday)

    lst = [3, 7, 2, 44, 11, 200, 99, 23, 55]
    mn, mx = min_max(lst)
    print(f'Min = {mn} Max = {mx}')

if __name__ == "__main__":
    main()
