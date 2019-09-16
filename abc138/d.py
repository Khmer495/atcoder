from collections import deque

n, q = [int(i) for i in input().split()]

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = [int(i) for i in input().split()]
    tree[a].append(b)
    tree[b].append(a)

counter = [0] * (n+1)
for _ in range(q):
    p, x = [int(i) for i in input().split()]
    counter[p] += x

queue = deque([[0,1]])
while queue:
    parent, node = queue.popleft()
    for leaf in tree[node]:
        if leaf == parent:
            continue
        counter[leaf] += counter[node]
        queue.append([node, leaf])

print(*counter[1:])
