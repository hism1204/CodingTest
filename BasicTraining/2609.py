l = list(map(int, input().split()))
num1 = l[0]
num2 = l[1]

def LeastCommonMultiple(num1,num2,GCD):
    return int((num1 / GCD) * (num2 / GCD) * GCD)
def GreatestCommonDivisor(num1,num2):
    divisor_num1 = []
    divisor_num2 = []
    for i in range(1,num1+1):
        if num1 % i == 0:
            divisor_num1.append(i)

    for i in range(1,num2+1):
        if num2 % i == 0:
            divisor_num2.append(i)

    return max(set(divisor_num1).intersection(set(divisor_num2)))
def main(num1,num2):
    GCD = GreatestCommonDivisor(num1,num2)
    LCM = LeastCommonMultiple(num1,num2,GCD)
    print(GCD)
    print(LCM)


main(num1,num2)