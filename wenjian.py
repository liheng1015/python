#!/home/student/nsd1905/bin/python
'''文档字符串

创建文件,如果文件已经存在,重新输入,如果不存在创建并输入数据,写入文件内
'''

import os

def get_fname():
    '返回文件名'
    while 1:
        fname = input('filename: ')
        if not os.path.exists(fname):     #os判断文件是否已经存在模块
            break
        print('文件已存在,请重试')

    return fname

def get_content():
    '返回内容'
    content = []                           #列表用于存放数据
    print('请输入数据,输入end结束')


    return content

def wfile(fname,content):
    '将内容content写入文件fname'
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname,content)
