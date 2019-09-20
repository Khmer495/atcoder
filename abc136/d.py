def main():
    s, = open(0).read().split()
    n = len(s)

    cnt = [0] * n
    stock_r_odd = 0
    stock_r_even = 0
    stock_l_odd = 0
    stock_l_even = 0
    for i in range(n):
        if s[i] == 'R':
            if s[i+1] == 'R':
                stock_r_even += 1
            else:
                cnt[i] += 1 + stock_r_even
                cnt[i+1] += stock_r_odd
                stock_r_odd = 0
                stock_r_even = 0
            stock_r_odd, stock_r_even = stock_r_even, stock_r_odd

        if s[-1-i] == 'L':
            if s[-1-i-1] == 'L':
                stock_l_even += 1
            else:
                cnt[-1-i] += 1 + stock_l_even
                cnt[-1-i-1] += stock_l_odd
                stock_l_odd = 0
                stock_l_even = 0
            stock_l_odd, stock_l_even = stock_l_even, stock_l_odd

    print(*cnt)
    return()

if __name__ == '__main__':
    main()
