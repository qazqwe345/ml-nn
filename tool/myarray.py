#-*- coding: utf-8 -*-

class MyArray:

    def __init__(self, array):
        self.array = array

    def add(self, value):
        self.array.append(value)
    
    def set_array(self, value):
        self.array = value

    def set(self, i, value):
        self.array[i] = value

    def len(self):
        return len(self.array)

    def __getitem__(self, i):
        return self.array[i]

    def sum(self):
        return sum(self.array)

    def __add__(self, arg):
        return self.calc(arg, lambda x,y:x+y)
    
    def __sub__(self, arg):
        return self.calc(arg, lambda x,y:x-y)

    def __rsub__(self, value):
        res = MyArray([])
        for i in range(self.len()):
            res.add(value - self.array[i])
    
        return res

    def __mul__(self, arg):
        return self.calc(arg, lambda x,y:x*y)

    def __rmul__(self, value):
        res = MyArray([])
        for i in range(self.len()):
            res.add(self.array[i] * value)

        return res

    def calc(self, arg, opt):
        res = MyArray([])
        for i in range(self.len()):
            res.add(opt(self.array[i], arg[i]))

        return res

    def __str__(self):
        return 'MyArray:' + str(self.array)


