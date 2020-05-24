def main():
    K, S = open(0).read().split()
    K = int(K)

    ans = ''
    len_S = len(S)
    if len_S <= K:
        ans = S
    else:
        ans = S[:K] + '.' * 3

    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
