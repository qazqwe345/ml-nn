
from tool.myarray import MyArray


def read(filename):
    res = []

    f = open(filename, 'r')

    for line in f:
        sp = line.strip().split(',')
        array = MyArray([float(x) for x in sp])

        res.append(array)

    f.close()

    return res
