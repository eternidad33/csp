n = int(input())
s = []
for i in range(n):
    s.append(input())
for a in s:
    a = a.replace("x", "*")
    a = a.replace("/", "//")
    sum_a = eval(a)
    if sum_a == 24:
        print("Yes")
    else:
        print("No")
