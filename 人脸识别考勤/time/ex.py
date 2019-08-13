
#   ctrl + z 返回键;   ctrl+/ 单行注释;  ctrl+d 复制一行
#   ctrl + x 剪贴      ctrl + s 保存
'''

1.环境变量的配置，开发工具的安装
2.第一个python文件运行：创建项目+创建文件夹+创建 python file
3.注释： 单行注释 # 和 多行注释  ''' '''
4.变量
5.流程控制语句（1.顺序语句 2.分支语句 3.循环语句）
6.面向对象
7.异常
8.文件读写
9.python连接数据库，mysql


变量：  变量名=值
数据类型： 整数，小数，字符，布尔类型，元组，字符串
'''
score=90
Score=90

c='男'
str='我叫小明'
flag=True
flag=False
print('姓名: %s 分数: %d'%(str,score))
print('姓名:',str,'分数:',score)
print(id(c))        # id()  地址
print(id(Score))
print(id(score))
Score=98
print(id(Score))
print('Hello,World!')

# 从控制台获取数据
'''
name=input('请输入姓名：')
print(name)
'''
a=98
b=69
c=a+b
c=a*b
c=a/b
print(c)
c=a//b
print(c)
c=a%b
print(c)
num=1
num+=2
print(num)
print(type(num))
'''
i=input('请输入数字:')
print(type(i))
a=int(i)
print(type(a))
print(type(eval(i)))
'''

