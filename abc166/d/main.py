import sys
INF = 10**9
sys.setrecursionlimit(INF)
import math


def main():
    x, = map(int, open(0).read().split())

    """
    x=a^5-b^5=(a-b)(a^4+a^3b+a^2b^2+ab^3+b^4)
    x//(a-b)=int>0
    a-b>0
    x=O(a^4)
    """

    for i in range(-1000, 1000 + 1):
        for j in range(-i + 1, i):
            if i**5 - j**5 == x:
                a = i
                b = j
                break

    ans = f'{a} {b}'
    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
