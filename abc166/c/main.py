import sys
INF = 10**9
sys.setrecursionlimit(INF)


def main():
    n, m, *hab = map(int, open(0).read().split())
    h = hab[:n]
    ab = hab[n:]
    ab = [[ab[2 * i] - 1, ab[2 * i + 1] - 1] for i in range(m)]

    ans_set = set(range(n))
    not_ans_set = set()
    # print(h)
    for a, b in ab:
        if h[a] >= h[b]:
            ans_set.discard(b)
            not_ans_set.add(b)
        if h[a] <= h[b]:
            ans_set.discard(a)
            not_ans_set.add(a)
        # print(a, b, ans_set, not_ans_set)

    ans = len(ans_set)
    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
