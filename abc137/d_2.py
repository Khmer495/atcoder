import heapq

def main():
    n, m, *ab = map(int, open(0).read().split())

    ab_dict = {}
    for a, b in zip(*[iter(ab)] * 2):
        if a > m:
            continue
        if a in ab_dict:
            ab_dict[a].append(-b)
        else:
            ab_dict[a] = [-b]

    cand = []
    ans = 0
    for day in range(1, m+1):
        if day in ab_dict:
            for cand_b in ab_dict[day]:
                heapq.heappush(cand, cand_b)
        if cand:
            ans += -heapq.heappop(cand)

    print(ans)
    return()

if __name__ == '__main__':
    main()
