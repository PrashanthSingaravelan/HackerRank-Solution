class Stack:
    def __init__(self):
        self.list1 = []
        self.ptr   = 0
    
    def Create(self,size):
        self.ptr = size-1
        
    def Push(self,element):
        self.list1.append(element)
    
    def Pop(self):
        self.ptr-=1
        return(self.list1.pop())
    
    def isEmpty(self):
        if self.list1 ==[]: return 1
        else:return 0


def isBalanced(str1):
    for i in range(len(str1)):
        if str1[i]=='{' or str1[i]=='[' or str1[i]=='(':   # Pushing all the elements into the stack
            obj1.Push(str1[i])
            print(obj1.list1)
        
        elif (obj1.isEmpty()!=1 and (                   # Before checking the condition, stack should not be empty
             (str1[i]==')' and obj1.list1[-1]=='(' or 
              str1[i]=='}' and obj1.list1[-1]=='{' or 
              str1[i]==']' and obj1.list1[-1]=='['))):  
                obj1.list1.pop()
        
        else: return "NO"                              # No matching from the string, directly return 'NO'
                
    if obj1.isEmpty():return "YES"
    else:return "NO"


obj1 = Stack()
n=int(input())
for i in range(n):
    str1 = input()
    print(isBalanced(str1))
    obj1.list1=[]