def main():
    k, x = map(int, open(0).read().split())

    min_black = max(-1000000, x - (k - 1))
    max_black = min(1000000, x + (k - 1))
    ans = range(min_black, max_black + 1)
    print(*ans)
    return()

if __name__ == '__main__':
    main()
