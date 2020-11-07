# 时间：2020.11.6 11点20分
# 活动安排问题
# 算法思想：贪心法
# 要求输出满足能安排的最多数目的活动安排序列
# 输入：第一行中给出待安排的活动数n，第二行开始，每行给出一个活动的开始时间和结束时间，一行内的数据用空格分隔。
# 输出：按格式从小到大依次输出相容活动编号（活动数据输入顺序为活动编号），各编号之间用逗号分割

# 注意：贪心算法有个对数据的预处理部分
# 贪心法求活动安排问题：
#       1.活动数据预处理（结束时间升序），排序后的编号也要保存
#       2.排序完成之后，扫描活动贪心则得到结果，注意结果是能够安排的最多的活动数

'''
    功能：对活动们进行数据的预处理：开始时间的升序排序
    传入活动，返回升序排序后的结果
    注意：排序后的活动编号也会随之改变，需要保存在一个编号向量中
'''
def ActivitysProcessing(activitys,serials):
    activity_len=len(activitys)

    # 排序
    for i in range(activity_len):
        temp_start=int(activitys[i][0][0])
        temp_end = int(activitys[i][0][1])
        for j in range(i+1,activity_len):
            follow_start=int(activitys[j][0][0])
            follow_end = int(activitys[j][0][1])
            # print("当前的结束时间：", temp_end, "比较的结束时间：", follow_end)
            if temp_end > follow_end:
                # print(">>>>当前的结束时间：",temp_end,"比较的结束时间：",follow_end)
                # print(">>>>当前需要交换的编号为：", i+1, "和：", j+1)

                # 交换位置:注意要是activity中的元素交换位置
                temp_s=temp_start
                activitys[i][0][0]=follow_start
                activitys[j][0][0]=temp_s

                temp_e=temp_end
                activitys[i][0][1]=follow_end
                activitys[j][0][1]=temp_e

                # 对应的活动下标位置交换
                temp_s=serials[i]
                serials[i] =serials[j]
                serials[j] =temp_s

                temp_end=follow_end

    return activitys


'''
    贪心法思想
    传入当前预处理好的活动activitys以及活动对应的编号向量serials
    返回选中的活动的编号向量：select_serials
    问题：需要每个都扫描，然后比较安排的最大活动值，待解决
'''
def GreedyAlgorithm(activitys,serials):
    # 存放活动的数组
    select_serials=[]
    length=len(activitys)


    start_time=int(activitys[0][0][0])
    end_time=int(activitys[0][0][1])
    # 初始位置从每一个开始
    for i in range(0,length):
        temp_select_serials=[]
        temp_select_serials.append(serials[i])

        for j in range(i+1,length):
            start_follow=int(activitys[j][0][0])
            end_follow = int(activitys[j][0][1])
            if start_follow >= end_time:
                # 满足相容条件
                temp_select_serials.append(serials[j])

                # 值的变换
                start_time,end_time=start_follow,end_follow

        temp_len=len(temp_select_serials)
        s_len=len(select_serials)
        if temp_len>s_len:
            select_serials=temp_select_serials

    return select_serials

'''
    打印活动
'''
def PrintActivity(activitys):
    for i in range(len(activitys)):
        # 使用贪心法，返回对应的活动编号,活动的个数，当前活动个数最大值，最大值所在下标
        print("当前编号：", (i + 1), "start:", activitys[i][0][0], "end:", activitys[i][0][1])


# 获取输入的数据
activity_numbers=int(input())
activitys=[]
for i in range(activity_numbers):
    activitys.append([input().split(" ")])

# 存放活动编号结果的容器
serials=[]
for i in range(activity_numbers):
    serials.append(i+1)

#print("------------数据预处理前----------------")
#PrintActivity(activitys)
#print("当前编号：",serials)

# 对活动们进行数据的预处理：开始时间的升序排序
activitys=ActivitysProcessing(activitys,serials)

#print("------------数据预处理后----------------")
#PrintActivity(activitys)
#print("当前编号：",serials)

select_serials=GreedyAlgorithm(activitys,serials)
sorted(select_serials)
# 按照格式输出
print("{",end="")
for i in range(len(select_serials)):
    if i!=len(select_serials)-1:
        print("%d," % select_serials[i],end="")
    else:
        print("%d" % select_serials[i],end="")
print("}")
