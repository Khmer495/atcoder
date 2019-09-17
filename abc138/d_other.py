from collections import deque
import sys

n, q, *args = map(int, open(0).read().split())
ab = args[:(n-1)*2]
px = args[(n-1)*2:]
print(n,q,ab,px)

tree = [[] for _ in range(n+1)]
for a, b in zip(*[iter(ab)]*2):
    tree[a].append(b)
    tree[b].append(a)

counter = [0] * (n+1)
for p, x in zip(*[iter(px)]*2):
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
