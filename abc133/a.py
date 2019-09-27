def main():
    n, a, b = map(int, open(0).read().split())

    ans = min(a * n, b)
    print(ans)
    return()

if __name__ == '__main__':
    main()
