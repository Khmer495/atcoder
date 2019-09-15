import bisect

n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]


while m > 0:
    a.sort()
    m -= 1
    a[-1] = a[-1] // 2
    for i in range(n-1)[::-1]:
        if m == 0:
            break
        if a[i] > a[-1]:
            m -= 1
            a[i] = a[i] // 2
        else:
            break

ans = sum(a)
print(ans)
