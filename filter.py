#!/home/student/nsd1905/bin/python
'''文档字符串

处理结果正确的,返回正确的列表

'''

from random import randint
def func1(x):
    return True  if x % 2 == 1 else False

if __name__ == '__main__':
    # print(func1(3))
    #True
    nums = [randint(1,100) for i in range(10)]
    print(nums)
    result = filter(func1,nums)
    print(list(result))
    result2 = filter(lambda x:True  if x % 2 == 1 else False,nums)
    print(list(result2))


    def func1(s):
        return s + '.com'


    if __name__ == '__main__':
        alist = ['qq', 'suhu', '163']
        result = map(func1, alist)
        print(list(result))
        result2 = map(lambda s: s + '.com', alist)
        print(list(result2))
