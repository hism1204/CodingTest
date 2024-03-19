l = list(map(int,input().split()))

num1 = l[0]
num2 = l[1]

def main():
    list = []
    loc = 0
    cnt = 1
    while(loc<num2):
        loc += cnt
        cnt += 1

    ##cnt-2까지는 모두 더함
    ##cnt-1번째 숫자는 몇번 더했는지 모름

    for i in range(1,cnt-1):
        for j in range(1,i+1):
            list.append(i)


    for k in range(1,num2 - (loc-cnt+1)+1):
        list.append(cnt-1)

    print(sum(list[num1-1:num2]))

    return

main()