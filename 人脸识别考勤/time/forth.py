 #  循环
'''
 循环：
 1.变量初始化
 2.循环条件
 3.变量的迭代
 4.代码段
 while 和 for 循环
 break,continue
'''
Sum=0
i=1
while i<=100:
    Sum+=i
    i+=1
print('Sum=',Sum)

sum=0
for i in range(100):
    sum+=i
print(sum)

for i in range(4):
    for j in range(i+1):
        print('*',end='')
    print()
i=0


while i<4:
    j=0
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i=i+1

# continue:跳过本次循环（继续执行）   和     break：跳出当前所在循环（终止）

for i in range(10):
    if i==5:
        continue;
    print('i=',i)
print()

for i in range(10):
    if i==5:
        break;
    print('i=',i)

