'''
try: try代码块，包含有可能出现异常的代码
except: try块中出错后，except块进行捕获
finally:有没有异常，finally块中的代码都会执行

'''

try:
    print(5/0)
except Exception as e:
    print(e)
finally:
    print('finally')

def write():
    f=open('D:/test.txt','w')
    f.write('abcdef')

def read():
    f=open('D:/test.txt','r')
    result=f.read()
    print(result)
write()
read()

