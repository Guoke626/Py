
class Father():
    def eat(self):
        print ('eat')
    def sleep(self):
        print('sleep')
class Boys(Father):
    def playGame(self):
        print('game')
class Girls(Father):
    def shopping(self):
        print('shopping')

'''
多重继承 class Boys(Father,Mother)
pass:占位功能

def add():
    pass
    
'''
jack=Boys()
jack.eat()


def method(n):
    if n==1:
        return 1
    else:
        return n*method(n-1)
result=method(5)
print(result)