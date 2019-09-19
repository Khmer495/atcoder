def main():
    a, b, c = map(int, open(0).read().split())

    ans = max(0, c - (a - b))
    print(ans)
    return()

if __name__ == '__main__':
    main()
