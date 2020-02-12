class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    

    def push(self,data):
        new_node=Node(data)
        temp=self.head
        new_node.next=self.head

        if (self.head is not None):
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
        else:
            new_node.next=new_node
            # self.head=new_node
        
        self.head=new_node
    
    def printList(self):
        temp=self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp=temp.next 
                if (temp==self.head):
                    break
    def tocircular(self,head):
        # head is the head reference
        start=head
        while(head.next is not None):
            head=head.next
        head.next=start
        return start
    
    def delete(self,del_value):

        curr_node=self.head
        prev_node=None
        while(curr_node):
                if curr_node.data==del_value and curr_node==self.head:
                    # case 1: Head is the only element in clist
                    if curr_node.next==self.head:
                        curr_node=None
                        self.head=None
                        return
                    # Case 2 : There are more elements in Clist
                    else:
                        # Traverse and update head & delete head
                        if curr_node.next != self.head:
                            curr_node=curr_node.next
                        curr_node.next=self.head.next
                        self.head=self.head.next
                        curr_node=None
                        return
                elif curr_node.data==del_value:
                    prev_node.next=curr_node.next
                    curr_node=None
                    return
                else:
                    if curr_node.next==self.head:
                        print("Value is not found")
                        break
                prev_node=curr_next
                curr_node=curr_node.next
    def countNode(self):
        curr=self.head
        self.count=1
        while(curr.next!=self.head):
            self.count=self.count+1
            curr=curr.next
        
        print("No of nodes is:",self.count)
    
    def getNodeCount(self,node):
        if(node.next==self.head):
            return 1
        return 1+ self.getNodeCount(node.next)

    def getCount(self):
        return self.getNodeCount(self.head)

    

myClist=CircularLinkedList()
myClist.push(1)
myClist.push(2)
myClist.push(3)
myClist.printList()
myClist.countNode()
print(myClist.getCount())