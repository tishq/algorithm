'''9、 素数问题
【问题描述】
打印出[m,n]之间的素数。
【输入】
m 和 n,m 小于等于 n。
【输出】
[m,n]之间的素数及其总数,具体格式见输出样例。
【输入样例】
100,120( 输入参考代码:m,n = eval(input('请输入 m 和 n:')) )
【输出样例】
101
103
107
109
113
The total is 5'''


m,n = eval(input('请输入 m 和 n:'))
flag = 1
prime = []

if m<3:
    m=3
    prime.append(2)

for p in range(m,n):
    for i in range(2,p-1):
        if(p%i==0):
            flag = 0
    if flag == 1:
        prime.append(p)
    else:
        flag = 1
for p in prime:
    print(p)
print('The total is %s' %(len(prime)))
