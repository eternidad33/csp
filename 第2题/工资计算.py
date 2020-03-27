t = int(input())
rate = [0, 0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
sA = [0, 1500, 4500, 9000, 35000, 55000, 80000, 100000]
afterTax = [3500]
sum = 0
for i in range(1, len(sA)):
    sum += int((sA[i] - sA[i - 1]) * (1 - rate[i]))
    afterTax.append(sum + 3500)
if t <= 3500:
    s = t
else:
    for i in range(len(afterTax)):
        if afterTax[i] < t < afterTax[i + 1]:
            s = 3500 + sA[i]
            s += int((t - afterTax[i]) / (1 - rate[i + 1]))
            s = 100 * (round(s / 100))
            break
print(s)
