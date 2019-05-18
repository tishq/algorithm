'''17、 整数移动
【问题描述】
有 n 个整数,使其前面各数顺序向后移 m 个位置,最后 m 个数变成最前面的 m 个数。
要求整数移动的功能单独用函数实现。
【输入】
输入 n 和 m,具体格式见输入样例。
【输出】
原始数据和移位后的数据,具体格式见输出样例。
【输入样例】
整数 n 为:8
向后移 m 个位置为:5
原始数据为:2 8 6 1 78 45 34 3
( 输入数据的参考代码如下:
n = int(input('整数 n 为:'))
m = int(input('向后移 m 个位置为:'))
number = list(map(int, input().strip().split())) #以空格输入若干数据存入列表
)
【输出样例】
原始列表: [2, 8, 6, 1, 78, 45, 34, 2]
移动之后:[1, 78, 45, 34, 3, 2, 8, 6]'''

n = int(input('整数 n 为:'))
m = int(input('向后移 m 个位置为:'))
number = list(map(int, input().strip().split())) #以空格输入若干数据存入列表
i=0
k=0
list2=[]
for num in number:
    list2.append(number[0])
    k=k+1
for num in number:
  if i+m>=n:
     j=i+m-n
     list2[j]=number[i]
  else :
     list2[i+m]=number[i]
  i=i+1
print(list2)
