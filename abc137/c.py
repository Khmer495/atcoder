from math import factorial

def main():
    n, *s = open(0).read().split()

    exist_s = {}
    for cur_s in s:
        cur_s = ''.join(sorted(list(cur_s)))
        if cur_s in exist_s:
            exist_s[cur_s] += 1
        else:
            exist_s[cur_s] = 1

    ans = 0
    for val in exist_s.values():
        if val < 2:
            continue
        ans += factorial(val) // (factorial(val - 2) * factorial(2))

    print(ans)
    return()

if __name__ == '__main__':
    main()
