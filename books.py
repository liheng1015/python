#!/home/student/nsd1905/bin/python
'''类

特殊方法如_init_ 实例化
        __str__ 显示实例自动调用
        __call__ 调用实例自动调用

'''

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author =author

    def __str__(self):
        return '<%s>' % self.title

    def __call__(self):
        print('<%s>是%s编著的' % (self.title,self.author))

if __name__ == '__main__':
    #实例化时自动调用_init_方法
    pybook = Book('python基础教程','Maguns Lie Hetland')
    print(pybook)  #显示实例时,自动调用_str_方法
    pybook()  #调用实例时,自动调用_call_方法

#:%s/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)$/\1:\2:\3:\4:\5:\6/
    
