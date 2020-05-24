
import math


def main():
    A, B, H, M = map(int, open(0).read().split())

    H_rasian = (H + M / 60) / 12 * 2 * math.pi
    M_rasian = M / 60 * 2 * math.pi
    ans = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos((H_rasian - M_rasian)))

    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
