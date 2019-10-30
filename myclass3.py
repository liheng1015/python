#!/home/student/nsd1905/bin/python
'''类

创建子类,子类的Warrior、Mage共用父类Role

'''

class Role:
    def __init__(self,nm,wp):
        self.nm = nm
        self.wp = wp

    def show_me(self):
        print('我是: %s,善用%s' % (self.nm,self.wp))

    def speak(self, word):
        print(word)

class Warrior(Role):
    def attack(self, dst):
        print('攻击: %s' % dst)

class Mage(Role):
    pass

if __name__ == '__main__':
    lb = Warrior('吕布','天方画戟')
    dc = Mage('貂蝉','吃')
    lb.show_me()
    dc.show_me()
    lb.speak('人在他在')
    dc.speak('我爱猴子')
    lb.attack('董卓')
