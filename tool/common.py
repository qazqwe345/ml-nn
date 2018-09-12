
import math
from tool import util
from tool.myarray import MyArray


def r_matrix(nrow, ncol):

    res = []

    for i in range(nrow):
        tmp = MyArray([])

        for j in range(ncol):
            tmp.add(util.r())

        res.append(tmp)

    return res


def init_m_layer(len_layer, len_row, len_col):
    m_layer = []

    for layer in range(len_layer):
        m_ws = r_matrix(len_row, len_col)
        m_layer.append(m_ws)

    return m_layer

def output(ws, inputs):
    outs = MyArray([])

    for w in ws:
        tmp1 = w * inputs
        tmp2 = tmp1.sum()
        tmp3 = sig(tmp2)

        outs.add(tmp3)

    return outs


def sig(num):
    return 1/(1+math.exp(-num))
