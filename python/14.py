'''14、 阶乘和(用函数实现)
【问题描述】
求 1+2!+3!+...+n!的和。
【输入】输入 n。
【输出】
1-n 的阶乘和,具体格式见输出样例。
【输入样例】
20
【输出样例】
1! + 2! + 3! + ... + 20! = 2561327494111820313'''


n=int(input())
q=0
for m in range(0,n):
 p=1
 for o in range(1,m+1):
  p=p*(o+1)
 q=q+p

print(q)


