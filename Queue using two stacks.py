class Queue():
    def __init__(self):
        self.list1 = []
        self.front = self.rear  = 0
    
    def Enqueue(self,element):
        self.list1.append(element)
        if len(self.list1)==1:
            self.front=self.rear=0
        else:
            self.rear+=1   
    
    def Dequeue(self):
        if self.rear==-1:
            print('There is no element in the queue')
        else:
            x = self.list1[self.front]
            self.list1.remove(self.list1[self.front])
    
    def Print(self):
        print(self.list1[self.front])
    
    def Display(self):
        print(*self.list1)

obj1 = Queue()
n=int(input())
for i in range(n):
    p=list(map(int,input().split()))
    choice = p[0]
    if choice==1:obj1.Enqueue(p[1])
    if choice==2:obj1.Dequeue()
    if choice==3:obj1.Print()