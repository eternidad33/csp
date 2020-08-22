def return_lend_key(key_info, times, time):
    RL_key = []
    for i in range(len(times)):
        if times[i] == time:
            RL_key.append(key_info[i][0])
    return RL_key


n, k = map(int, input().split())
info = []
for i in range(k):
    info.append(list(map(int, input().split())))
key = list(range(1, n + 1))

# 分别存储开始使用时间和归还时间
start_time = [i[1] for i in info]
end_time = [i[1] + i[2] for i in info]

for t in range(1, max(end_time) + 1):
    # 先还后借
    # t时刻为归还时间
    if t in end_time:
        return_key = return_lend_key(info, end_time, t)
        return_key.sort()
        for r in return_key:
            for i in range(n):
                if key[i] == 0:
                    key[i] = r
                    break
    # t时刻为借用时间
    if t in start_time:
        lend_key = return_lend_key(info, start_time, t)
        for r in lend_key:
            for i in range(n):
                if key[i] == r:
                    key[i] = 0
print(' '.join(map(str, key)))
