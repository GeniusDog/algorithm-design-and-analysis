# 时间：2020.10.10 13点46分
# 描述：输出双递归函数Ackerman函数A(n，m)的结果
# 输入：在一行中输入2个正整数A和B，并用空格分隔。
# 输出Ackerman函数值。

def getAckerman(n,m):
    '根据计算公式，得到函数结果'
    if n==1 and m==0:
        return 2
    if n==0 and m>=0:
        return 1
    if m==0 and n>=2:
        return n+2
    if m>=1 and n>=1:
        return getAckerman(getAckerman(n-1,m),m-1)


input_number=input().split(" ")
n=int(input_number[0])
m=int(input_number[1])
result=getAckerman(n,m)
print(result)
