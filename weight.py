
from myarray.myarray import MyArray

inputs = [MyArray([1,1]),
          MyArray([2,1]),
          MyArray([3,1]),
          MyArray([4,1]),
          MyArray([5,1]),
          MyArray([6,1])]

w = MyArray([-1,-1])

correct = MyArray([-1,-1,-1,-1,1,1])

rate = 0.2

def output(w, input):

    tmp = w*input

    return 1 if tmp.sum() > 0 else -1

def learn(w, rate, x, flag):
    flgs = MyArray([flag, flag])

    return (w+rate*flgs*x)

for count in range(100):

    loop = False

    for (i, value) in enumerate(inputs):
        out = output(w, value)
        if out != correct.v(i):
            loop = True
            w = learn(w, rate, value, correct.v(i))

    if not loop:
        print (count)
        break

for (i, value) in enumerate(inputs):
    print (output(w, value))

print (output(w, MyArray([-10,1])))
print (output(w, MyArray([7,1])))
