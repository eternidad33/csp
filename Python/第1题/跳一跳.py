a = list(map(int, input().split()))
n = len(a)
score, temp = 0, 2
for i in range(n):
    if a[i] == 0:
        break
    elif a[i] == 1:
        score += 1
        temp = 2
    else:
        if a[i - 1] == 1 or i == 0:
            score += 2
            temp += 2
        else:
            score += temp
            temp += 2
print(score)
