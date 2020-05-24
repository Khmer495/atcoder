def main():
    n, = map(int, open(0).read().split())
    first_place_of_n = n % 10

    ans = ''
    if first_place_of_n in [2, 4, 5, 7, 9]:
        ans = 'hon'
    elif first_place_of_n in [0, 1, 6, 8]:
        ans = 'pon'
    else:
        ans = 'bon'

    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
