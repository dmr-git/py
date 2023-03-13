#!/usr/bin/env python3

while True:
    name1 = input(" Please give me a name (first last): ")
    name2 = input(" Please give me another name (first last): ")

    fn1 = name1.split(" ")[0]
    ln1 = name1.split(" ")[1]

    fn2 = name2.split(" ")[0]
    ln2 = name2.split(" ")[1]

    # combine first half of fn1 with second half of fn2
    fn3 = fn1[0 : (len(fn1) // 2)]
    fn4 = fn2[(len(fn2) // 2) :]
    outf1 = fn3 + fn4

    # combine first half of fn2 with second half of fn1
    fn3 = fn2[0 : (len(fn2) // 2)]
    fn4 = fn1[(len(fn1) // 2) :]
    outf2 = fn3 + fn4

    # combine first half of ln1 with second half of ln2
    ln3 = ln1[0 : (len(ln1) // 2)]
    ln4 = ln2[(len(ln2) // 2) :]
    outl1 = ln3 + ln4

    # combine first half of ln2 with second half of ln1
    ln3 = ln2[0 : (len(ln2) // 2)]
    ln4 = ln1[(len(ln1) // 2) :]
    outl2 = ln3 + ln4

    print(outf1.capitalize(), outl1.capitalize())
    print(outf2.capitalize(), outl2.capitalize())
