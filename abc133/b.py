def main():
    n, d, *x = map(int, open(0).read().split())

    cnt = 0
    for j in range(n):
        for i in range(j):
            y = x[i*d:(i+1)*d]
            z = x[j*d:(j+1)*d]
            dist_double = 0
            for cur_y, cur_z in zip(y, z):
                dist_double += (cur_y - cur_z) ** 2
            dist = int(dist_double ** 0.5 + 0.5)
            if dist ** 2 == dist_double:
                cnt += 1

    ans = cnt
    print(ans)
    return()

if __name__ == '__main__':
    main()
