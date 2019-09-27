def main():
    n, *a = map(int, open(0).read().split())

    # b[0] == a[0] - a[1] + a[2] - a[3] + ...
    b = [sum(a) - 2 * sum(a[1::2])]

    for cur_a in a[:-1]:
        b.append(cur_a * 2 - b[-1])

    ans = b
    print(*ans)
    return()

if __name__ == '__main__':
    main()
