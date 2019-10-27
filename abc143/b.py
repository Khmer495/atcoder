def main():
    n, *d = map(int, open(0).read().split())

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)
    return()

if __name__ == '__main__':
    main()
