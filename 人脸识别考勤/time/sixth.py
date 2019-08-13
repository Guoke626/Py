
from fifth import Person1

def add(a,b,c):
    print(a,b,c)
    return a+b+c

def test():
    add(1,4,8)                 #如果在一个类里面则()里用self,   self.add()


result=add(1,2,3)
print(result)

p=Person1('tom',12)
p.eat()
