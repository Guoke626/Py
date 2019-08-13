
#  分支语句 if if……else if ……elif ……else
'''
格式：
if  表达式:
    代码段

'''
score=98
list=[90,98,76,88]
if score>90:
    print('优秀')
print('over')

if score in list:
    print('True')
print('over')

if score>=90:
    print('优秀')
elif score>=80 and score<90:  # 不能用 if 80<score<90:
    print('良好')
else:
    print('不优秀')
print('over')
