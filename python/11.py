'''11、 自由落下的小球
【问题描述】
一球从 100 米高度自由落下,每次落地后反跳回原高度的一半;再落下,求它在第 n
次落地时,共经过多少米?第 n 次反弹多高?
【输入】
输入 n。
【输出】
小球第 n 次落地时共经过的距离以及第 n 次反弹多高,具体格式见输出样例。
【输入样例】
10
【输出样例】
总高度:tour = 299.609375
第 10 次反弹高度:height = 0.09765625'''


n=int(input())
ht=0
hn=100
for i in range(n):
    hn = hn / 2
    if i==0:
        ht=100
    else:
        ht+=hn*2*2
print('总高度:tour =%s' %(ht))
print('第 %s 次反弹高度:height =%s' %(n,hn))
