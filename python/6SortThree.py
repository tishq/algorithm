'''6、 三个整数排序
【问题描述】
输入三个整数 x,y,z,请把这三个数由小到大输出。
【输入】
三个整数,具体格式见输入样例。
【输出】
以列表形式输出由小到大排序的三个整数,具体格式见输出样例。
【输入样例】
请输入三个整数:
8
5
6
【输出样例】
[5, 6, 8]'''



input('请输入三个整数: ')
a=int(input())
b=int(input())
c=int(input())
if a>b:
    t=a
    a=b
    b=t
if b>c:
    t=b
    b=c
    c=t
if a > b:
    t = a
    a = b
    b = t
print('[%s,%s,%s]' % (a,b,c))
