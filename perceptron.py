
import myfile as file
from myarray import MyArray

correct = file.read('correct.csv')
inputs = file.read('data.csv')

x = MyArray([-1,-1,-1])
rate = 0.2

def output(w, x):

    tmp = w * x
    value = tmp.sum()

    return (1 if value>=0 else -1)

def learn(w, rate, x, flg):
    return (w + rate * flg * x)

for (i, value) in enumerate(inputs):
    print (output(w, value))

for count in range(1):

    for (i,value) in enumerate(inputs):
        out = output(w, value)

        if out != correct[i].v(0):
            w = learn(w, rate, value, correct[i].v(0))

for (i, value) in enumerate(inputs):
    print (output(w, rate))


