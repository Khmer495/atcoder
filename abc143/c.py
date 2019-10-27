def main():
    n, s = open(0).read().split()
    n = int(n)

    before_s = ''
    ans = 0
    for _s in s:
        if _s != before_s:
            ans += 1
            before_s = _s
        else:
            continue
    print(ans)
    return()

if __name__ == '__main__':
    main()
