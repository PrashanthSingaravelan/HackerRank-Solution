def GCD(a,b):
     
    # Everything divides 0
    if (b == 0):
         return a
    return GCD(b, a%b)

def LCM(num1, num2):
    
    if (num1 == 0 or num2 == 0):
        return 0
    
    else:
        if (num1>num2): gcd = GCD(num1,num2)
        else: gcd = GCD(num2,num1)
    
        lcm = int ( (num1 * num2) / gcd )
        return lcm


def between_two_sets(list1, list2):
    num1 = list1[0]
    num2 = list1[1]

    lcm = LCM(num1, num2)
    for i in range(2, len(list1)):
        lcm = LCM(lcm, list1[i])

    print("LCM of list-1 : ",lcm)

    num1 = list2[0]
    num2 = list2[0]

    gcd = GCD(num1, num2)
    for i in range(2, len(list2)):
        gcd = GCD(gcd, list2[i])

    print("GCD of list-2 : ",gcd)

    ## common multiples of lcm that divideds the gcd by 1
    cnt = 0
    multiple = 0
    while (multiple <= gcd):
        multiple += lcm

        if (gcd % multiple == 0):
            cnt+=1
    
    return cnt

if __name__ == '__main__':
    n,m = input().split()
    n, m = int(n), int(m)

    list1 = list(map(int , input().split()))
    list2 = list(map(int , input().split()))    

    print(between_two_sets(list1, list2))