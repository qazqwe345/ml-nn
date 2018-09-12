
import copy
from tool import util, common, myfile
from tool.myarray import MyArray


class Unit:

    def __init__(self):

        self.m_outs = []
        self.out = MyArray([])

    def initialize(self, len_unit, len_w, len_layer, len_m_unit, len_m_w):
        
        self.m_layer = common.init_m_layer(len_layer, len_m_unit, len_m_w)
        self.ws = common.r_matrix(len_unit, len_w)

    def process_output(self, inputs, in_row):
        self.m_outs = []
        a = inputs[in_row]

        for m_ws in self.m_layer:
            a = common.output(m_ws, a)
            a.add(1)
            self.m_outs.append(a)

        self.out = common.output(self.ws, a)

    def process_update_weight(self, rate, correct, inputs, in_row):
        m_layer_update = copy.deepcopy(self.m_layer)

        out_delta = -1 * (correct[in_row] - self.out) * self.out * (1 - self.out)
        
        delta_L1 = out_delta
        w_L1 = self.ws

        for layer in reversed(range(len(self.m_layer))):
            m_ws = copy.deepcopy(self.m_layer[layer])
            delta_L = MyArray([])
            delta_L.set_array([0] * len(m_ws))
            
            for i in range(len(m_ws)):
                m_out_tmp = self.m_outs[layer]
                tmp1 = 0

                for k in range(delta_L1.len()):
                    tmp1 = tmp1 + delta_L1[k] * w_L1[k][i] * m_out_tmp[i] * (1 - m_out_tmp[i])
                delta_L.set(i, tmp1)

                for j in range(m_ws[0].len()):
                    m_out_L_1 = 0

                    if layer == 0:
                        m_out_L_1 = inputs[in_row][j]

                    else:
                        m_out_L_1 = self.m_outs[layer-1][j]

                    tmp2 = m_ws[i][j] - rate * delta_L[i] * m_out_L_1
                    m_layer_update[layer][i].set(j, tmp2)

            delta_L1 = delta_L
            w_L1 = m_ws
            self.m_layer = m_layer_update

        for i in range(len(self.ws)):
            for j in range(self.ws[i].len()):

                tmp3 = self.ws[i][j] - rate * out_delta[i] * self.m_outs[-1][j]
                self.ws[i].set(j, tmp3)
