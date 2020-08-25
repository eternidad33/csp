n = int(input())
a = list(map(int, input().split()))


def 最大的矩形(count, l):
    """思路：遍历每个矩形向左右延伸的最大面积"""
    b = []  # 储存所有局部最大矩形
    for i in range(count):
        width = 0  # 矩形宽度
        for j in reversed(range(i)):  # 向左（反转）搜索左边高度不小于矩形i高度的
            if l[j] >= l[i]:
                width += 1  # 加左边宽度
            else:
                break
        for j in range(i, count):  # 向右搜索高度不小于矩形i高度的
            if l[j] >= l[i]:
                width += 1  # 加右边宽度（含矩形i自身）
            else:
                break
        b.append(l[i] * width)  # 得到包含矩形i自身的局部最大矩形面积
    print(max(b))  # 从所有局部最大矩形选出全局最大举行


最大的矩形(n, a)
