n = int(input())
q = list(range(1, n + 1))
m = int(input())
for i in range(m):
    k, t = map(int, input().split())
    after = q.index(k) + t
    q.remove(k)
    q.insert(after, k)
print(' '.join(map(str, q)))
