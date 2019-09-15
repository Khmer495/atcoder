n = int(input())
h = [int(i) for i in input().split()]

cur_list = [h[0]]
ans = 0
for cur_h in h[1:]:
    if cur_list[-1] >= cur_h:
        cur_list.append(cur_h)
    else:
        ans = max(ans, len(cur_list) - 1)
        cur_list = [cur_h]
ans = ans = max(ans, len(cur_list) - 1)

print(ans)
