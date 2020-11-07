# 时间：2020.10.10 14点24分
# 描述：请编写程序输出前n个正整数的全排列（n<10），并通过9个测试用例（即n从1到9）观察n逐步增大时程序的运行时间
# 输入：输入给出正整数n（<10）。
# 输出：输出1到n的全排列。每种排列占一行，数字间无空格。排列的输出顺序为字典序
# 改良版：解决内存超限问题
import itertools


def Permutation(numbers):
    "对元素进行全排列，并将结果保存在一个列表中返回"
    result=[]
    numbers_len=len(numbers)

    if numbers_len==1:
        #当集合中只有它自身的时候，返回自己
        return  [numbers]
    else:
        for i in numbers:
            # 遍历每一个元素，得到当前字符和其他字符集合
            temp=numbers.copy()
            temp.remove(i)

            # 递归关键步骤：ri Prem(temp)
            result +=[[i] + k for k in Permutation(temp)]

    return  result

#获取输入值n
n=int(input())

#根据输入获取元素集合
numbers=list(range(1, n + 1))

'''

# 对元素进行全排列，并将结果输出
result_Permutation=Permutation(numbers)
for i in result_Permutation:
    # 列表里保存的是“嵌套”的结果，所有需要处理一下：循环输出每一个
    print("".join([str(n) for n in i]))

'''

#改良版：解决内存超限问题，调用自带的工具
result=list(itertools.permutations(numbers, n))

#输出结果
for i in result:
    # 列表里保存的是“嵌套”的结果，所有需要处理一下：循环输出每一个
    print("".join([str(n) for n in i]))

