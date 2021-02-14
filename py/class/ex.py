class Person:
    role = 'person' #人的角色都是人
    def __init__(self,name):
        self.name = name #每一个角色都有自己的名字

    def walk(self): #人能走路
        print("person is walking")

print(Person.role) #查看人的role属性
print(Person.walk) #引用人走路方法而不是调用

egg = Person('egon')
print(egg.name)
print(egg.walk())
