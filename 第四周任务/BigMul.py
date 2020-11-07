# 时间：2020.10.19 01点43分
# 描述：完成大整数乘法
# 方法：取位相乘，移位相加
# 公式：XY=ac * 10 ^2m + ((a+b)(c+d)-ac-bd) * 10 ^ m +bd
#       X=a*10^m+b      Y=c * 10^m +d
# 问题：生成新的部分 (a+b)(c+d)，获取高分位困难
# 采用公式：XY=ac * 10 ^2m + (a*d+b*c) * 10 ^ m +bd


# 将大数分割成对应的部分,返回列表，分别是：a,b,高分位，数字长度
def getAttrByNumber(number):
    # 获取长度
    length=len(str(number))

    # 数字a对应的高分位
    high=length // 2

    # 对应的a,b,high,length保存在一个列表中
    result=[]
    x=int(number)
    result.append(x // 10 **high)
    result.append(x % 10 ** high)
    result.append(high)
    result.append(length)

    return  result



# 大整数乘法：分治，递归，合并
def bigMul(number_x,number_y):
    # 首先获取输入两个数据的长度，已经对应的a,b,c,d
    x_attr=getAttrByNumber(number_x)
    y_attr=getAttrByNumber(number_y)

    # 如果分割是最简形式，直接得结果
    x_len=int(x_attr[3])
    y_len=int(y_attr[3])
    if x_len==1 or y_len==1:
        return int(number_x) * int(number_y)
    else:
        # 对数字继续进行分割 XY=ac * 10 ^2m + (a*d+b*c) * 10 ^ m +bd
        a_c=bigMul(x_attr[0],y_attr[0])
        b_d=bigMul(x_attr[1],y_attr[1])
        a_d=bigMul(x_attr[0],y_attr[1])
        b_c=bigMul(x_attr[1],y_attr[0])
        ac_high=int(x_attr[2])+int(y_attr[2])
        ad_high=int(x_attr[2])
        bc_high=int(y_attr[2])

        # 注意这里的m是数字对应的高分位，因此对公式的化简需要注意
        return a_c * (10 ** ac_high) +a_d * (10 ** ad_high) +b_c * (10 ** bc_high) +b_d


# 获取输入
number_x=input()
number_y=input()

# 对输入数据进行大整数乘法并输出
result=bigMul(number_x,number_y)
print(result)
