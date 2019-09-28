import bisect

def main():
    n, k, *h = map(int, open(0).read().split())
    h.sort()
    k_index = bisect.bisect_left(h, k)
    ans = n - k_index
    print(ans)
    return()

if __name__ == '__main__':
    main()
