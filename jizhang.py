#!/home/student/nsd1905/bin/python
'''文档字符串

记账程序
'''
import os
import pickle
from time import strftime

def save(fname):
    try:
        amount = int(input('金额: '))
        comment = ('备注: ')
    except ValueError:
        print('')
        return
    except (KeyboardInterrupt, EOFError):
        print()
        return

    date = strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount

    record = [date,amount,0,balance,comment]
    records.append(record)
    with open(fname,'wb') as fobj:
        pickle.dump(records,fobj)


def cost(fname):
    try:
        amount = int(input('金额: '))
        comment = ('备注: ')
    except ValueError:
        print('')
        return
    except (KeyboardInterrupt, EOFError):
        print()
        return

    date = strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount

    record = [date,amount,0,balance,comment]
    records.append(record)
    with open(fname,'wb') as fobj:
        pickle.dump(records,fobj)


def cost(fname):
    try:
        amount = int(input('金额: '))
        comment = ('备注: ')
    except ValueError:
        print('')
        return
    except (KeyboardInterrupt, EOFError):
        print()
        return

    date = strftime('%Y-%m-%d')
    with open(fname,'rb') as fobj:
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount

    record = [date,0,amount,balance,comment]
    records.append(record)
    with open(fname,'wb') as fobj:
        pickle.dump(records,fobj)
        
def query(fname):
    #取出所有表记录
    with open(fname,'rb') as fobj:
        records = pickle.load(fobj)

    #打印表头
    print('%-16s%-8s%-8s%-10s%-20s' % ('date','save','cost','balance','comment'))
    for record in records:
        print('%-16s%-8s%-8s%-10s%-20s' % tuple(record))

def show_menu():
    cmds = {'0':save,'1':cost,'2':query}
    prompt = '''(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    fname = 'account.data'
    init_data = [['2019-10-14',0,0,10000,'init']]

    if not os.path.exists(fname):
        with open(fname,'wb') as fobj:
            pickle.dump(init_data,fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'
        if choice not in ['0','1','2','3']:
            print('无效的输入,请重试.')
            continue

        if choice == '3':
            print('\nbye-bye')
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
                                                                                                                                            94,1         底端


