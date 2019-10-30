#!/home/student/nsd1905/bin/python
'''文档字符串

异常错误处理,不同的错误,打印一样的输出,可以把报错村变量打印出来
'''

try:
    n = int(input('number: '))
    result = 100 / n

except (ValueError,ZeroDivisionError) as e: #把异常保存到变量e中
    print('无效的输入', e)
except (KeyboardInterrupt,EOFError):
    print('\nBye-bye')
    exit()         #直接跳出,但是执行finally
else:            #只有正常才执行
    print(result)
finally:
    print('Done')        #正常和异常都执行

print('结束')
