#!/usr/bin/env python3

# Filename:     drutils_tst.py
# Author:       DMR

import sys


def main():
    """
    This is the main function.  It will be used to call the various examples.
    """
    from drutils import get_date

    bday = get_date()
    print(bday)


if __name__ == "__main__":
    main()
