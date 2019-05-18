'''10、 分数序列(要求程序中使用元组)
【问题描述】
有一分数序列:2/1,3/2,5/3,8/5,13/8,21/13......求出这个数列的前 n 项之和。
【输入】
输入 n,表示所要求的数列的前 n 项。
【输出】
前 n 项的和,具体格式见输出样例。
【输入样例】
20
【输出样例】
32.6602607986'''


n=int(input())
a=1
b=2
sum=0
for i in range(n):
    sum += (b/a)
    t=a
    a=b
    b=a+t
print(sum)
