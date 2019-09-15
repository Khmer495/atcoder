n = int(input())
b = [int(i) for i in input().split()]

a = [b[0]]
for i in range(len(b)-1):
    a.append(min(b[i], b[i+1]))
a.append(b[-1])

ans = sum(a)
print(ans)
