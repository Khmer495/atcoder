def main():
    a, b = map(int, open(0).read().split())

    ans = max(0, a - b * 2)
    print(ans)
    return()

if __name__ == '__main__':
    main()
