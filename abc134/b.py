def main():
    n, d = map(int, open(0).read().split())

    ans = -(-n // (d*2+1))
    print(ans)
    return()

if __name__ == '__main__':
    main()
