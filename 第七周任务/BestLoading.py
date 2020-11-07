# 时间：2020.11.7 21点55分
# 最优装载问题
# 输入：输入有2行数据，第一行是n和C值，用空格分隔，第二行是是n个整数表示的wi，用空格分隔。
# 输出：按照输入集装箱重量的顺序输出n个用空格分隔的Y或N。
#       Y表示该集装箱被选中，N表示不被选中。
#       最后一行输出所选中的集装箱的总重量w和个数num,用空格分隔。
# 算法思想：贪心法

'''
    功能：对箱子的重量进行升序排序，对应的编号也改变
    返回：箱子重量的升序排列和对应的编号
'''
def ProcessBoxs(boxs,boxs_numbers,length):
    for i in range(length):
        min=int(boxs[i])
        for j in range(i+1,length):
            temp=int(boxs[j])
            if temp < min:
                min=temp
                boxs[i],boxs[j]=boxs[j],boxs[i]
                boxs_numbers[i],boxs_numbers[j]=boxs_numbers[j],boxs_numbers[i]
    return boxs,boxs_numbers

'''
    功能：贪心法求最优装载问题
    传入：排序后的箱子重量向量，对应的箱子编号向量，需要标记的flag.以及集装箱的负载量
    返回：显示结果的flag向量。装载箱子的重量和个数
'''
def GreedyLoading(boxs,boxs_numbers,flag,weight):
    load_weight=0
    load_count=0

    current_weitht=weight-load_weight
    i=0
    while(current_weitht>= int(boxs[i])):
        # 标记对应的箱子
        flag[int(boxs_numbers[i])-1]=1

        # 箱子装船，总负载变化
        current_weitht=current_weitht-int(boxs[i])
        load_weight += int(boxs[i])
        load_count += 1

        i+=1

    return flag,load_weight,load_count
# 获取数据
n,weight=input().split(" ")
boxs=input().split(" ")

# 为箱子生成对应的编号
boxs_numbers=[i for i in range(1,int(n)+1)]

# 箱子的标记向量
flag=[0 for i in range(int(n))]

# 预处理：重量排序，注意编号也对应
boxs,boxs_numbers=ProcessBoxs(boxs,boxs_numbers,int(n))
#print("boxs:",boxs)
#print("numbers:",boxs_numbers)

# 贪心算法求可以装载的箱子
flag,load_weight,load_count=GreedyLoading(boxs,boxs_numbers,flag,int(weight))

# 输出对应的是否可以装载结果，以及装载重量和个数
for i in range(int(n)):
    if i != (int(n)-1):
        if flag[i]==0:
            print("N ",end="")
        else:
            print("Y ",end="")
    else:
        if flag[i]==0:
            print("N")
        else:
            print("Y")
print(load_weight,load_count)
