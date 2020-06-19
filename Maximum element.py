class Stack:
    def __init__(self):
        self.Normal_list = []
        self.Maximum_list = []
   
    def Push(self,element):                 
        self.Normal_list.append(element)
        if not self.list2 or (element>=self.Maximum_list[-1]):
            self.Maximum_list.append(element)
    
    def Pop(self):
        value = self.Normal_list.pop()
        if value == self.Maximum_list[-1]:
            self.Maximum_list.pop()
        
    def PrintMax(self):
        print(self.Maximum_list[-1])

obj1 = Stack()
n=int(input())

for i in range(n):
    p = list(map(int,input().split()))
    choice = p[0]
    if choice==1:
        element = p[1]
        obj1.Push(element)
    elif choice==2:obj1.Pop()
    else:obj1.PrintMax()

'''
def Push() 
1) Accepting the element in Normal list
2) if there are no other elements in the list (or) the element to be added must be greate than Maximum_list[-1]
   then add that element in Maximum list

def Pop()
1) Poping the element from Normal list
2) if the popped element == Main_list[-1], then the Main_list's last element should also be popped 