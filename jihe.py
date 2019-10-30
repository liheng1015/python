#!/home/student/nsd1905/bin/python
'''文档字符串

用集合文件去重,a.log和b.log,取出只有在b.log的行
'''

with open('/etc/passwd') as f1:
    s1 = set(f1)

with open('/tmp/mima') as f2:
    s2 = set(f2)

s2 - s1

with open('/tmp/result.txt','w') as f3:
    f3.writelines(s2 - s1)
