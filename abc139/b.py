import math

a, b = [int(i) for i in input().split()]

ans = math.ceil((b-1) / (a-1))

print(ans)
