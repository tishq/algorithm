'''12、 统计不同类型的字符
【问题描述】
输入一行字符,分别统计出其中英文字母、空格、数字和其它字符的个数。
【输入】
一行字符。
【输出】
分别输出英文字母、空格、数字和其它字符的个数,具体格式见输出样例。
【输入样例】
123runoobc kdf235*(dfl
【输出样例】
char = 13,space = 2,digit = 6,others = 2'''


str = input()
alphaNum=0
numbers=0
spaceNum=0
otherNum=0
for i in str:
    if i.isalpha():
        alphaNum +=1
    elif i.isnumeric():
        numbers +=1
    elif i.isspace():
        spaceNum +=1
    else:
        otherNum +=1
print('char = %d,'%alphaNum,'space = %d,'%spaceNum,'digit = %d,'%numbers,'others %d'%otherNum)





