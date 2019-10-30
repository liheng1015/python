#!/home/student/nsd1905/bin/python
'''类

多重继承

'''

class A:
    def funca(self):
        print('class a')

    def func1(self):
        print('aaaaaaaaaaaaaaa')

class B:
    def funcb(self):
        print('class b')

    def func1(self):
        print('bbbbbbbbbbbbbb')

class C(A, B):
    def funcc(self):
        print('class c')

    def func1(self):
        print('cccccccccccc')

if __name__ == '__main__':
    c1 = C()
    c1.funca()
    c1.funcb()
    c1.funcc()
    c1.func1()
~                
