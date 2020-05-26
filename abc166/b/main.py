import sys
INF = 10**9
sys.setrecursionlimit(INF)


def main():
    n, k, *da = map(int, open(0).read().split())

    is_have_list = set()

    for _ in range(k):
        d = da.pop(0)
        for _ in range(d):
            is_have_list.add(da.pop(0))

    ans = n - len(is_have_list)
    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
