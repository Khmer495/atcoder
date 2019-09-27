def main():
    l, r = map(int, open(0).read().split())
    MOD = 2019
    if r - l >= MOD:
        print(0)
        return()
    l %= MOD
    r %= MOD
    if l == 0 or r == 0:
        print(0)
        return()
    if l >= r:
        r += MOD

    ans = float('inf')
    for i in range(l, r):
        for j in range(i+1, r+1):
            ans = min(ans, (i * j) % MOD)

    print(ans)
    return()

if __name__ == '__main__':
    main()
