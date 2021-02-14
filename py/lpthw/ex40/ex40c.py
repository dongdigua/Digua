class mystuff(object):

    def __init__(self):
        self.tangerine = 'haha' #python创建的空对象self，可以对其进行操作
        #这里self设置成了一段话
    def apple(self):
        print('I am apple')
#将self赋给thing
thing = mystuff() #就是类似于调用mystuff.py一样，在init对thing进行初始化,
#这行就像import mystuff
thing.apple()
print(thing.tangerine)
