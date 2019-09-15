n = int(input())
s = input()

ans = 0

while ans <= len(s)//2:
    prev_s = ''
    for i in range(ans+1, len(s)//2+1):
        if s[:i] in s[i:]:
            prev_s = s[:i]
        else:
            ans = max(ans, len(prev_s))
            break
    else:
        ans = max(ans, len(prev_s))
    s = s[1:]
    if len(s) == 1:
        break

print(ans)
