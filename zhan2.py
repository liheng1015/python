#!/home/student/nsd1905/bin/python
'''文档字符串

用列表构造栈结构
'''
stack = []
def push_it():
    data = input('请输入数据:')
    if data:
        stack.append(data)
    # print('push')

def pop_it():
    if stack:
        print('从栈中弹出:\033[31;1m%s\033[0m' % stack.pop())
    else:
        print('\033[34;1m栈已经为空\033[0m')
    # print('pop')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    #cmds = {'0':push_it,'1':pop_it,'2':view_it}
    cmds = {push_it, pop_it,view_it}
    prompt = '''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3):'''
    while 1:
        choise = input(prompt).strip()
        if choise not in ['0','1','2','3']:
            print('无效输入请重试')
            continue

        if choise == '3':
            print('bybe---bybe')
            break
            
        int(choise)
        cmds[choise]()

if __name__ == '__main__':
    show_menu()
                       
