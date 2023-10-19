
n = int(input())
arr = []
_xarr = []
_yarr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    _xarr.append(a)
    _yarr.append(b)

ans = [-1] * n

for sx in _xarr:
    for sy in _yarr:
        dist = []
        for ex, ey in arr:
            d = abs(ex - sx) + abs(ey - sy)
            dist.append(d)
        dist.sort()
        temp = 0
        for i in range(len(dist)):
            d = dist[i]
            temp += d
            if ans[i] == -1: ans[i] = temp
            else: ans[i] = min(temp, ans[i])

print(*ans)