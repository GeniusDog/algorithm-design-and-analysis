# 时间：2020.10.10 13点15分
# Fibonacci数列
# 输入一个正整数n (1<=n<=40)。
# 次输出：Fn
# Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
# 改良版：解决超时问题——创建一个列表，将前40项放入列表中

def GetFibonacciList():
    #保存返回结果的列表
    result=[1,1]
    for i in range(2,41):
        result.append(result[i-1]+result[i-2])
    return  result

number=int(input(""))
list=GetFibonacciList()
number_Fi=list[number-1]

#print("当前的斐波拉列数列数字是：",number_Fi)
print(number_Fi)

