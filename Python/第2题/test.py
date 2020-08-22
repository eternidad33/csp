# 公共钥匙盒

# 找出要借，或者要还的钥匙编号
def return_lend_key(info, time):
    RL_key = []
    for i in range(0, len(time)):
        if time[i] == t:
            RL_key.append(info[i][0])
    return RL_key


n, k = input().split()
n = int(n)
k = int(k)
key = [i for i in range(1, n + 1)]  # 钥匙盒
info = [[0 for i in range(3)] for j in range(k)]  # 存放钥匙使用情况

for i in range(k):
    info[i][:] = [int(wsc) for wsc in input().split()]

for i in range(k):
    info[i][2] = info[i][1] + info[i][2]

start_time = [i[1] for i in info]  # 二维列表切片操作
end_time = [i[2] for i in info]

for t in range(1, max(end_time) + 1):
    # 先还后借
    # 还
    if t in end_time:
        return_key = return_lend_key(info, end_time)  # 找出要还的钥匙
        return_key.sort()
        for r in range(len(return_key)):
            for i in range(n):
                if key[i] == 0:
                    key[i] = return_key[r]
                    break
    # 借
    if t in start_time:
        lend_key = return_lend_key(info, start_time)  # 找出要借的钥匙
        for r in range(len(lend_key)):
            for i in range(n):
                if key[i] == lend_key[r]:
                    key[i] = 0

for i in key:
    print(i, end=' ')