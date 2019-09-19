def main():
    n, *h = map(int, open(0).read().split())

    prev_h = h[-1]
    for cur_h in h[::-1][1:]:
        diff_h = cur_h - prev_h
        if diff_h > 1:
            print('No')
            return()
        prev_h = cur_h
        if diff_h == 1:
            prev_h -= 1

    print('Yes')
    return()

if __name__ == '__main__':
    main()
