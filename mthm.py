#!/usr/bin/env python3
'''
   convert minutes to hours/minutes
   Pass the number of minutes on the command line
'''

import sys

x = int(sys.argv[1])
 
print(f"{x} minutes is equivalent to {x//60} hours and {x%60} minutes.")


