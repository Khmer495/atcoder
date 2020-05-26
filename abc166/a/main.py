import sys
INF = 10**9
sys.setrecursionlimit(INF)


def main():
    s, = open(0).read().split()

    ans = 'ARC' if s == 'ABC' else 'ABC'
    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
