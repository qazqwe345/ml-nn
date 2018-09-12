
from tool import myfile

rate = 0.03
max = 5000
len_data = 3
len_correct = 2

correct = myfile.read('correct.csv')
input_data = myfile.read('data.csv')

len_layer = 3 #number of hidden layers
len_m_w = len_data
len_m_unit = len_m_w - 1
len_unit = len_correct
len_w = len_m_unit + 1
