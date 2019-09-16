n = int(input())
v = [int(i) for i in input().split()]

v.sort()

for i in range(len(v)-1):
    v[-1-i] /= 2**(i+1)
v[0] /= 2**(len(v)-1)

ans = sum(v)

print(ans)
