n = int(input())
a = [int(i) for i in input().split()]

ans = 0
for a_i in a:
    ans += 1 / a_i

ans = 1 / ans

print(ans)
