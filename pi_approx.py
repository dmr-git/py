#!/usr/bin/env python3

# Author: DMR

import os
from math import pi

def p_pi(s1,p):
    print(s1, "=\t{0:.70f}".format(p))
    
def main():
    os.system("clear")
    p =pi
    p_pi("math.pi",p)
    p = 256/81
    p_pi("256/81",p)
    print('')
   

if __name__ == '__main__':
    main()