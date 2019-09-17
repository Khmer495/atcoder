from bisect import bisect_left as bisect

def main():
    n, m, *ab = map(int, open(0).read().split())

    rate = []
    for a, b in zip(*[iter(ab)] * 2):
        if a > m:
            continue
        rate.append([a, b])

    rate = sorted(rate, key=lambda x: -x[1])

    day = list(range(1, m + 1))
    day_len = m
    ans = 0
    for term, money in rate:
        work_day = bisect(day, term)
        if work_day == day_len:
            continue
        else:
            del day[work_day]
            day_len -= 1
            ans += money

    print(ans)
    return()

if __name__ == '__main__':
    main()
