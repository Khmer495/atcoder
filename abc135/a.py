def main():
    a, b = map(int, open(0).read().split())

    k = a + (b - a) / 2
    if k == int(k):
        k = int(k)
        print(k)
    else:
        print('IMPOSSIBLE')
    return()

if __name__ == '__main__':
    main()
