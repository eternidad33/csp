n, k = map(int, input().split())
key = list(range(1, n + 1))
info = []
for i in range(k):
    info.append(list(map(int, input().split())))

start_time = [i[1] for i in info]
end_time = [i[2] for i in info]


def return_lend_key(info, time):
    RL_key = []
    for i in range(len(time)):
        if time[i] == t:
            RL_key.append(info[i][0])
    return RL_key


for t in range(1, max(end_time) + 1):
    if t in end_time:
        return_key = return_lend_key(info, end_time)
        return_key.sort()
        for r in return_key:
            for i in range(n):
                if key[i] == 0:
                    key[i] = r
                    break
    if t in start_time:
        lend_key = return_lend_key(info, start_time)
        for r in lend_key:
            for i in range(n):
                if key[i] == r:
                    key[i] = 0
print(' '.join(map(str, key)))
