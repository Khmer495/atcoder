def main():
    n, *a = map(int, open(0).read().split())

    sorted_a  = sorted(a)
    max_a = sorted_a[-1]
    next_max_a = sorted_a[-2]
    for cur_a in a:
        if cur_a == max_a:
            print(next_max_a)
        else:
            print(max_a)
    return()

if __name__ == '__main__':
    main()
