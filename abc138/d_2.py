from collections import deque
import sys
s = sys.stdin.readlines()

n, q = map(int, s[0].split())

tree = [[] for _ in range(n+1)]
for ab in s[1:n]:
    a, b = map(int, ab.split())
    tree[a].append(b)
    tree[b].append(a)

counter = [0] * (n+1)
for px in s[n:]:
    p, x = map(int, px.split())
    counter[p] += x

# pop, appendまたはQueueライブラリだと間に合わない
queue = deque([[0,1]])
while queue:
    parent, node = queue.popleft()
    for leaf in tree[node]:
        if leaf == parent:
            continue
        counter[leaf] += counter[node]
        queue.append([node, leaf])

print(*counter[1:])
