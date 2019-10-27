import bisect

def main():
    n, *l = map(int, open(0).read().split())
    l = sorted(l, reverse=True)

    ans = 0
    for a_i in range(n-2):
        a = l[a_i]
        b_i = a_i + 1
        c_i = n - 1
        while b_i < c_i:
            b = l[b_i]
            c = l[c_i]
            if a < b + c:
                b_i += 1
                ans += c_i - b_i + 1
            else:
                c_i -= 1
    print(ans)
    return()

if __name__ == '__main__':
    main()
