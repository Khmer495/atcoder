def force_select(a, c, cost):
    while c:
        for key, _c in c.items():
            if len(_c) == 1:
                _a = a.pop(key)
                cost += _a[0]
                rem = _a[1]
                for _rem in rem:
                    del c[_rem]
                break
        else:
            break
    return(a, c, cost)

def main():
    n, m, *abc = map(int, open(0).read().split())

    a = {}
    c = {}
    for i in range(n):
        c[i] = []
    init = 0
    for i in range(m):
        _a = abc[init]
        _b = abc[init+1]
        _c = [j-1 for j in abc[init+2:init+2+_b]]
        init = init + 2 + _b
        a[i] = [_a, _c]
        for __c in _c:
            c[__c].append(i)

    for _c in c.values():
        if len(_c) == 0:
            print(-1)
            return()

    cost = 0
    a, c, cost = force_select(a, c, cost)

    while c:
        for key, _c in c.items():
            min_cost = 10**6
            for __c in _c:
                min_cost = min(min_cost, a[__c][0])
            cost += min_cost
    ans = cost
    print(ans)
    return()

if __name__ == '__main__':
    main()
