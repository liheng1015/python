'''打印星号

这是一个演示用的模块,只包含了一个全局变量和一个函数
'''

hi = 'hello world'
def pstar(n=30):
    '缺省打印30个星号'
    return '*' * n

if __name__ == '__main__':
    print(hi)
    print(pstar(40))
