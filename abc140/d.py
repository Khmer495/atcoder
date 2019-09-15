n, k = [int(i) for i in input().split()]
s = input()

l_r = 0
r_l = 0
prev_s = s[0]
ans = 0
for cur_s in s[1:]:
    if prev_s == cur_s:
        ans += 1
    elif cur_s == 'L':
        r_l += 1
    else:
        l_r += 1
    prev_s = cur_s

if min(l_r, r_l) >= k:
    ans += 2 * k
else:
    ans += 2 * min(l_r, r_l)
    if max(l_r, r_l) >= k:
        ans += k - min(l_r, r_l)
    else:
        ans += max(l_r, r_l) - min(l_r, r_l)

print(ans)
