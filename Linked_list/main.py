class SinglyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)


head=SinglyNode(1)
A=SinglyNode(3)
B=SinglyNode(5)
C=SinglyNode(7)
        
    
head.next=A
A.next=B
B.next=C

# print(head)

curr=head
while(head):
    print(curr)
    curr=curr.next