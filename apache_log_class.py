#!/home/student/nsd1905/bin/python
'''apache的log oop形式,使用类
    显示出不同IP访问的次数,和不同浏览器访问的次数
    并排序字典

'''

import re
class CountPatt:
    def __init__(self,fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_dict = {}
        cpatt = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m: #如果匹配到为真,匹配不到为假
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+.){3}\d+' #1234.5678.10.8
    br = 'Firefox|MSIE|Chrome'
    cp = CountPatt(fname)
    result1 = cp.count_patt(ip)
    result2 = cp.count_patt(br)
    print(result1)
    print(result2)
    result3 = list(result1.items())
    result3.sort(key=lambda seq: seq[-1], reverse=True)
    print(result3)
    result4 = list(result2.items())
    result4.sort(key=lambda seq: seq[-1], reverse=True)
    print(result4)
