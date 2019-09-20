def main():
    n, *ab = map(int, open(0).read().split())
    a = ab[:n+1]
    b = ab[n+1:]

    init_a_sum = sum(a)
    for i, cur_b in enumerate(b):
        if a[i] > cur_b:
            a[i] -= cur_b
        else:
            a[i+1] = max(0, a[i+1] -  (cur_b - a[i]))
            a[i] = 0
    last_a_sum = sum(a)
    ans = init_a_sum - last_a_sum
    print(ans)
    return()

if __name__ == '__main__':
    main()
