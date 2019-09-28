def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    prime_divisors = []
    for i, _divisors in enumerate(divisors[::-1]):
        for _remain_divisors in divisors[::-1][i+1:][:-1]:
            if _divisors % _remain_divisors == 0:
                break
        else:
            prime_divisors.append(_divisors)
    return prime_divisors

def main():
    a, b = map(int, open(0).read().split())

    div_a = make_divisors(a)
    div_b = make_divisors(b)

    cnt = 0
    for _div_a in div_a:
        if _div_a in div_b:
            cnt += 1

    ans = cnt
    print(ans)
    return()

if __name__ == '__main__':
    main()
