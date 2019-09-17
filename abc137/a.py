def main():
    a, b = map(int, open(0).read().split())

    add = a + b
    sub = a - b
    mult = a * b

    ans = max(add, sub, mult)
    print(ans)
    return()

if __name__ == '__main__':
    main()
