#!/home/student/nsd1905/bin/python
'''文档字符串

找出某个时间段的log
2019-05-15 07:20:00 aa
2019-05-15 08:10:00 bb
2019-05-15 09:03:00 cc
2019-05-15 10:10:00 dd
2019-05-15 12:02:00 ee
2019-05-15 13:01:00 hh
'''

from datetime import datetime

t9 = datetime.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
t12 = datetime.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')

with open('/tmp/log1') as a:
    for line in a:
        t = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t > t9:
            print(line,end='')
##############################################################
#第二种方式
#!/home/student/nsd1905/bin/python
'''文档字符串

找出某个时间段的log
2019-05-15 07:20:00 aa
2019-05-15 08:10:00 bb
2019-05-15 09:03:00 cc
2019-05-15 10:10:00 dd
2019-05-15 12:02:00 ee
2019-05-15 13:01:00 hh
'''

import time

t9 = time.strptime('2019-05-15 09:00:00','%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-05-15 12:00:00','%Y-%m-%d %H:%M:%S')

with open('/tmp/log1') as a:
    # c = a.read()
    # print(c)
    for line in a:
        t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t > t9:
            print(line,end='')
