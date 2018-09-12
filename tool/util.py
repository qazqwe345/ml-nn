
import random


def r():
    return random.uniform(-1, 1)

def diff(correct, out):
    tmp = correct - out
    res = tmp * tmp
    return res.sum()

def puts(myarrays):
    print ('List [ MyArray ]: [')

    for myarray in myarrays:
        print (myarray)

    print (']')
