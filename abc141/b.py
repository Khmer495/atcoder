def main():
    s = input()

    ans = 'Yes'

    for odd_s in s[::2]:
        if odd_s not in ['R', 'U', 'D']:
            ans = 'No'
            return(ans)

    for even_s in s[1:][::2]:
        if even_s not in ['L', 'U', 'D']:
            ans = 'No'
            return(ans)

    return(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
