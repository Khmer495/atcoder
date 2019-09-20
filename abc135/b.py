def main():
    n, *p = map(int, open(0).read().split())

    cnt = 0
    for i, cur_p in enumerate(p):
        if i + 1 != cur_p:
            cnt += 1
        if cnt > 2:
            print('NO')
            return()
    print('YES')
    return()

if __name__ == '__main__':
    main()
