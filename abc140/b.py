n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

prev_a = -1
ans = 0
for i_a in a:
    ans += b[i_a-1]
    if i_a - prev_a == 1:
        ans += c[prev_a-1]
    prev_a = i_a

print(ans)
