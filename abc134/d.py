def main():
    n, *a = map(int, open(0).read().split())

    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n+1)[::-1]:
        if i * 2 > n:
            b[i] = a[i]
        else:
            rem = 0
            for j in range(i * 2 , n + 1, i):
                rem = rem ^ b[j]
            b[i] = rem ^ a[i]

    b = b[1:]
    m = sum(b)
    print(m)
    for i, cur_b in enumerate(b, start=1):
        if cur_b == 1:
            print(i, end=' ')
    return()

if __name__ == '__main__':
    main()
