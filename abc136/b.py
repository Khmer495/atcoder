import math

def main():
    n, = map(int, open(0).read().split())

    digit = math.floor(math.log10(n)) + 1

    ans = 0
    for i in range(1, digit + 1, 2):
        if i == digit:
            ans += n - 10**(i-1) + 1
        else:
            ans += 10**i - 10**(i-1)
    print(ans)
    return()

if __name__ == '__main__':
    main()
