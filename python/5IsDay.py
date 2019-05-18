'''5、 判断是第几天(要求程序中使用列表或元组数据类型)
【问题描述】
输入某年某月某日,判断这一天是这一年的第几天。
【输入】
年月日,具体格式见输入样例。
【输出】这一天是这一年的第几天。
【输入样例】
请输入年月日:2015 6 7(三个数据以空格分隔)
( 输入参考代码:year,month,day = map(int,input('请输入年月日:').split()) )
【输出样例】
It is the 158th day.'''



dat = input('请输入年月日: ')
y,m,d=map(int,dat.split()) # 获取年月日

ly = False
if y%100 == 0: # 若年份能被100整除
    if y%400 == 0: # 且能被400整除
        ly = True # 则是闰年
    else:
        ly = False
elif y%4 == 0: # 若能被4整除
     ly = True # 则是闰年
else:
    ly = False

if ly == True: # 若是闰年，则二月为29天
    ms = [31, 29, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
days = 0

for i in range(1,13): # 从1到12判断，已确定月份
    if i == m:
        for j in range(i-1): # 确定月份i之后，则将ms列表中的前i-1项相加
           days += ms[j]
        print('It is the %sth day.' % ((days +d)))
