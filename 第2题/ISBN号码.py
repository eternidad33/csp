s = input()


def backlist(s):
    rlist = []
    for i in s:
        if i.isdigit():
            rlist.append(int(i))
    return rlist


l = backlist(s)
sum = 0
for i in range(9):
    sum += l[i] * (i + 1)
code = sum % 11
if s[-1] == str(code) or (s[-1] == 'X' and code == 10):
    print("Right")
else:
    if code == 10:
        s = s[:-1] + 'X'
    else:
        s = s[:-1] + str(code)
    print(s)
