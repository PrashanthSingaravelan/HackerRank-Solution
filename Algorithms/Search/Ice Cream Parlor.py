def icecreamParlor(balance, flavors):
    dict1 = {}
    ans   = []
    
    for index, flavor_price in enumerate(flavors):
        
        difference = balance-flavor_price

        if difference not in dict1:
            dict1[flavor_price] = index+1
        
        elif difference in dict1:
            
            flavor1 = dict1[difference]
            flavor2 = index+1
            
            ans.append(flavor1)
            ans.append(flavor2)

            return ans
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr    = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        print(*result)