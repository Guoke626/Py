'''
1.先从控制台输入年和月

2.算出输入的年份到1900年多少天 365 366

3.算出当前的1月份距离输入的月份有多少天   月份计算（28,29,30,31）

4.打印输出
'''

year_now=int(input('请输入当前年份:'))
month_now=int(input('请输入当前月份:'))
date_now=int(input('请输入当前日期:'))

initial_year=1900
disyear=int(year_now-initial_year)                              # disyear 为该年与1900年的差
if disyear//4==0:
    disdate=disyear*366                                         # disdate 为该年1月1号与1900年1月1号相差天数

else:
    disdate=disyear*365


if month_now==1:
    disdate_now=date_now
elif month_now==2:
    disdate_now=31+date_now
elif month_now==3:
    if disyear // 4 == 0:
        disdate_now=31+29+date_now                                # disdate_now 为输入日期与输入的年份的1月1日相差天数

    else:
        disdate_now=31+28+date_now
elif month_now==4:
    if disyear // 4 == 0:
        disdate_now=31+29+31+date_now

    else:
        disdate_now=31+28+31+date_now
elif month_now==5:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+date_now

    else:
        disdate_now=31+28+31+30+date_now
elif month_now==6:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+31+date_now

    else:
        disdate_now=31+28+31+30+31+date_now
elif month_now==7:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+31+30+date_now

    else:
        disdate_now=31+28+31+30+31+30+date_now
elif month_now==8:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+31+30+31+date_now

    else:
        disdate_now=31+28+31+30+31+30+31+date_now
elif month_now==9:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+31+30+31+31+date_now

    else:
        disdate_now=31+28+31+30+31+30+31+31+date_now
elif month_now==10:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+31+30+31+31+30+date_now

    else:
        disdate_now=31+28+31+30+31+30+31+31+30+date_now
elif month_now==11:
    if disyear // 4 == 0:
        disdate_now=31+29+31+30+31+30+31+31+30+31+date_now

    else:
        disdate_now=31+28+31+30+31+30+31+31+30+31+date_now
else:
    if disyear // 4 == 0:
        disdate_now = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30+date_now

    else:
        disdate_now = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30+date_now

sum_disdate=disdate+disdate_now

if month_now==1 or month_now==3 or month_now==5 or month_now==7 or month_now==8 or month_now==10 or month_now==12:
    monthdate=31
elif month_now==4 or month_now==6 or month_now==9 or month_now==11:
    monthdate=30
else:
    if disyear // 4 == 0:
        monthdate=29

    else:
        monthdate=28

weekday_now=sum_disdate%7+1
weekday_initial=(sum_disdate-date_now+1)%7+1
print('该月份一号是星期',weekday_initial)
print('今天星期',weekday_now)
print('万年历如下：')
print('   ')
print('%d年%d月%d日'%(year_now,month_now,date_now))
print('    一    二   三   四   五   六   日')
if (weekday_initial+1)%7==1:
    print('   ',end='')
for j in range(weekday_initial):
    print('%4s'%(' '),end='')


for i in range(monthdate):
    weekday=(weekday_initial+i)%7
    if weekday!=1:
        print('%5d'%(i+1),end='')
    elif weekday==1:
        print()
        print('%5d'%(i+1), end=' ')










