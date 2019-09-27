def main():
    n, *a = map(int, open(0).read().split())

    b = [cur_a*2 for cur_a in a]

    c = [0]
    for cur_b in b:
        c.append(cur_b - c[-1])
    compensation = c.pop(-1) // 2
    c = [cur_c + compensation * (-1) ** in_i for in_i, cur_c in enumerate(c)]

    ans = c
    print(*ans)
    return()

if __name__ == '__main__':
    main()
