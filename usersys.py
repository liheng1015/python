#!/home/student/nsd1905/bin/python
'''文档字符串

模拟用户登录信息系统
'''
# import getpass
#
# usesys = {}
# def int_user():
#     uname = input('username:').strip()
#     if not uname:
#         print('用户名不能为空')
#         return
#
#     #用户不存在时询问密码,并写入字典
#     if uname in usesys:
#         print('用户已经存在')
#     else:
#         upass = input('password: ')
#         usesys[uname] = upass
#         print('用户注册成功')
#
# def login():
#     uname = input('username:').strip()
#     upass = getpass.getpass('password: ')
#    #if uname in userdb and userdb[uname] == upass:
#     if usesys.get(uname) == upass:
#         print('您登陆成功')
#     else:
#         print('您登录失败')
#
# def show_user():
#     cmds = {'0': int_user, '1': login}
#     prompt='''(0) 用户注册
# (1) 用户登录
# (2) 退出
# 请选择(0/1/2):'''
#     while 1:
#         user_int = input(prompt).strip()
#         if user_int not in ['0','1','2']:
#             print('-'*30+'\n请重新输入有效数字(0/1/2).')
#             continue
#
#         if user_int == '2':
#             print('bybe---bybe')
#             break
#
#         cmds[user_int]()
#
# if __name__ == '__main__':
#     show_user()
