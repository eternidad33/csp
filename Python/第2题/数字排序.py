def shuZiPaiXu(nums):
    nums.sort()
    a = {}
    for i in nums:
        a[i] = nums.count(i)
    # 排序
    a = sorted(a.items(), key=lambda item: item[1], reverse=True)
    for j in a:
        print(j[0], j[1])


n = int(input())
ls = list(map(int, input().split()))
shuZiPaiXu(ls)
# 12
# 5 2 3 3 1 3 4 2 5 2 3 5
