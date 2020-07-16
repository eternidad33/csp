y = int(input())
d = int(input())
mon = 0
md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    md[2] = 29
for i in md:
    if d - i > 0:
        d -= i
        mon += 1
    else:
        break
print(mon)
print(d)
