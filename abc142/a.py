def main():
    n, = map(int, open(0).read().split())

    ans = ((n+1) // 2) / n
    print(ans)
    return()

if __name__ == '__main__':
    main()
