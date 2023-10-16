class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printingLinkedList(self):
        temp=self.head
        while temp:
            if temp.next:
                print(temp.data,end='->')
            else:
                print(temp.data)
            temp=temp.next
    def hasCycle(self,head):
        slow=fast=head
        c=0
        flag=False
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            c+=1
            # print(slow.data,fast.data)
            if slow==fast:
                meet=fast
                # print(c)
                flag=True
                break
        start=head
        if flag:
            while start.next!=meet.next:
                start=start.next
                meet=meet.next
            if start!=meet:
                meet.next=None
            else:
                for i in range(c-1):
                    meet=meet.next
                meet.next=None
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node1.next=node2
node2.next=node3
# Creating a loop
node3.next=node4
node4.next=node1
LL=LinkedList()
LL.head=node1
LL.hasCycle(LL.head)
LL.printingLinkedList()