n, k, q = [int(i) for i in input().split()]
a = [int(input()) for _ in range(q)]

point = [k-q]*n

ans_point = [0]*n
for cur_a in a:
    ans_point[cur_a - 1] += 1

point = [point[i] + ans_point[i] for i in range(n)]

for cur_point in point:
    if cur_point > 0:
        print('Yes')
    else:
        print('No')
