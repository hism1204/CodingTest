l =list(map(int,input().split()))
val1 = l[0]
val2 = l[1]


def main():
    cnt = 0
    for i in range(1, val1 + 1):
        if val1 % i == 0:
            cnt += 1
            if cnt == val2:
                print(i)
                return
    print(0)
    return


main()