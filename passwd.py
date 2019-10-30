
import random
from string import ascii_letters,digits
s2=ascii_letters + digits
s1='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def passwd(n=8):
    passwd2 = ''
    for i in range(n):
        passwd1=random.choice(s1)
        passwd2 += passwd1
    return passwd2

if __name__ == '__main__':
    n=int(input('请输入密码长度:'))
    print(passwd(n))
    # if n == '':
    #     print(passwd())
    # elif isinstance(n,str):
    #     while 1:
    #         if isinstance(n, int):
    #             print(passwd(n))
    #             break
    #         else:
    #             print('请输入密码长度数字')
    #             n = input('请输入密码长度:')
    # else:
    #     n=int(n)
    #     print(passwd(n))
                           
