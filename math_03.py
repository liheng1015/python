#!/home/student/nsd1905/bin/python
'''文档字符串

算数
# 1 + 1 = 2
# very good
# Continue(y/n)? y
# 12+23 = 1
# wrong
# 12 + 23 = 2
# wrong
# 12 + 23 = 3
# wrong
# 12 + 23 = 35
# Continue(y/n)? n
# Bye-bye

'''

# from random import randint, choice
from random import randint,choice

# def add(x,y):
#     return x + y
#
# def sub(x,y):
#     return x - y

def exam():
    cmds = {'+': lambda x, y: x + y,'-': lambda x, y: x - y}
    nums = [randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')

    # if op == '+':
    #     result = add(*nums)
    # else:
    #     result = sub(*nums)
    result = cmds[op](*nums)

    counter = 0
    while counter < 3:
        prompt = '%s %s %s =' % (nums[0],op,nums[1])
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer == result:
            print('输入正确,太棒了!')
            break

        print('不对吆!')
        counter += 1
    else:
        print('%s%s' % (prompt,result))

def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nbye-bye')
            break

if __name__ == '__main__':
    main()
                     
