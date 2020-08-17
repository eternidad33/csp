n = int(input())
l = list(map(int, input().split()))
# 先将数据转成集合，然后再转成列表
s = list(set(l))
# t用于记录s中元素在l出现的次数
t = []
for x in s:
    t.append(l.count(x))
# t中最大值对应的索引即为所求
print(s[t.index(max(t))])
