def main():
    n, *a = map(int, open(0).read().split())

    ans = [0] * n
    for i, _a in enumerate(a):
        ans[_a-1] = i+1
    print(*ans)
    return()

if __name__ == '__main__':
    main()
