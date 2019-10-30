#!/home/student/nsd1905/bin/python
'''文档字符串

创建用户并随机生成8位密码
'''

import sys
import random
import subprocess

s1='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

def passwd(n=8):
    passwd2 = ''
    for i in range(n):
        passwd1=random.choice(s1)
        passwd2 += passwd1
    return passwd2

def userad(userna,password,file='/tmp/user.txt'):
    us=subprocess.run('useradd %s' % userna, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if us.returncode == 0:
        subprocess.run('echo %s | passwd --stdin %s' % (password,userna), shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print('创建用户成功\n密码并保存到%s' % file)
        with open(file,'a') as fobj:
            fobj.write('%s:%s\n' % (userna,password))
    else:
        print('您创建的%s已存在' % userna)
        return

if __name__ == '__main__':
    # username = sys.argv[1]
    # file = sys.argv[2]
    password = passwd()
    userad(sys.argv[1],password,'/tmp/user.txt')
