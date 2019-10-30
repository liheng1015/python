#!/home/student/nsd1905/bin/python
'''类

组合应用

'''

class Wp:
    def __init__(self,nm,type):
        self.wname = nm
        self.type = type

class Role:
    def __init__(self,nm,wp):
        self.nm = nm
        self.wp = wp
    def show_me(self):
        print('我是: %s,善用%s' % (self.nm,self.wp))

if __name__ == '__main__':
    #
    ji = Wp('天方画戟','物理攻击')
    lb = Role('吕布',ji)
    print(ji.wname,ji.type)
    print(lb.wp.wname,lb.wp.type)
