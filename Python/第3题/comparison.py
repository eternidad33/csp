# 最大矩形

# 输入
n = int(input())
a = list(map(int, input().split()))

'''
另一种思路，搜索矩形i向右的局部最大矩形
tempmax = 0
for i in range(len(a)):
    h=a[i]
    for l in range(len(a)-i):

        if(h>a[i+l]):
            h = a[i+l]
        if(h == 1):
            break
        tempmax = tempmax if(tempmax> h*(l+1)) else h*(l+1)
tempmax = tempmax if(tempmax> len(a)) else len(a)
print(tempmax)
'''

b = []  # 储存所有局部最大矩形
for i in range(len(a)):
    width = 0  # 矩形宽度
    for j in reversed(range(i)):  # 向左（反转）搜索左边高度不小于矩形i高度的
        if a[j] >= a[i]:
            width += 1  # 加左边宽度
        else:
            break;
    for j in range(i, len(a)):  # 向右搜索高度不小于矩形i高度的
        if a[j] >= a[i]:
            width += 1  # 加右边宽度（含矩形i自身）
        else:
            break;
    b.append(a[i] * width)  # 得到包含矩形i自身的局部最大矩形面积
print(max(b))  # 从所有局部最大矩形选出全局最大举行
