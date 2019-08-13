# 面向对象 特征(属性) 和 功能（函数，方法）组成，实实在在存在的实物
#   类： 是相同对象特征和功能的集合，是抽象的，模板
#  属性定义：1.在类中直接定义（变量）
#            2.在_init_方法中定义，初始化
'''
    函数定义
    格式： def 方法名（self，[参数1，参数2……]）
    返回结果： 1.不返回  2.通过return返回
    对象的创建： 对象名=类名()
    属性的调用：对象名.属性名
    方法的调用：对象名.方法名()

'''

class Person:
     name=None
     age=0
     def eat(self):
         print('eat……')
'''
对象创建   对象名=类名()
'''

p1=Person()
p1.name='白小龙'
p1.age=3
print(p1.name)
print(p1.age)
p1.eat()


class Person1:
    def __init__(self,m,n):
        self.name1=m
        self.age1=n
    def eat(self):
        print('eat ')
    def add(self,num1,num2):
        return num1+num2
    def method(self,n1,*args):                   # *  表示列表  可变形参
        print(n1,args)
    def method2(self,n1,**a):
        print(a)                                 # ** 表示字典

    @staticmethod                                #定义静态方法   静态方法不需要创建对象就可以调用
    def sum(a,b):
        print(a,b)
Person1.sum(1,2)
'''

p2=Person1('we',1)
p2.name='zh'
print(p2.name1)
print(p2.age1)
p2.eat()
result=p2.add(123,456)
print(result)
p2.method(1,34,56,78)
p2.method2(1,name='xiaoming',age=18)
'''




