def Consolidated_Height(list1):
    for i in range(1,len(list1)):
        if i<=len(list1):
            list1[i] = list1[i]+list1[i-1]
    return list1    

def Check(list1,list2,list3):
    while(True):
        
        # If any stack is empty
        if (list1==[] or list2==[] or list3==[]):
            return 0
        
        value1 = list1[-1]
        value2 = list2[-1]
        value3 = list3[-1]
    
        # If the heights of all the three stacks are equal
        if (value1==value2==value3): 
            return value1
    
        if (value1>=value2) and (value1>=value3):list1.pop()
        if (value2>=value1) and (value2>=value3):list2.pop()
        if (value3>=value1) and (value3>=value2):list3.pop()
        
n1,n2,n3 = input().split()

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = list(map(int,input().split()))

list1.reverse()
list2.reverse()
list3.reverse()

list1,list2,list3 = Consolidated_Height(list1) , Consolidated_Height(list2) , Consolidated_Height(list3)
print(Check(list1,list2,list3))