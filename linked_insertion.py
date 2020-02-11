class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node


    def insertAt(self,previousNode,newNode):
        temp = self.head

        while temp:
            if temp.data == previousNode:
                holdNext = temp.next
                newNode = Node(newNode)
                newNode.next = holdNext
                temp.next = newNode
                return
            temp = temp.next

        print("No Node found")

    def append(self, new_value):
        new_value = Node(new_value)

        if self.head is None:
            self.head = new_value
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_value

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next
    
    def deleteNode(self,key):
        temp=self.head

        if (temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
        
        while(temp is not None):
           
            if(temp.data==key):
                #  print(temp.data)
                #  print(key)
                 break
            prev=temp
            temp=temp.next
        if temp is None:
            print("Linked List is empty")
            return
        prev.next=temp.next
        temp=None
    
    def deleteTotalList(self):
        curr=self.head

        while(curr):
            next=curr.next
            self.head=next
            del curr.data
            curr=next

    def nodeCount(self,node):
        if(not node):
            return 0
        else:
            return 1+ self.nodeCount(node.next)
    
    def getCount(self):
        return self.nodeCount(self.head)
    
    def iterativeCount(self):
        curr=self.head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        print("No of nodes is: ",count)

    def reverseLinkedList(self):
        prev=None
        next=None
        curr=self.head
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

if __name__=='__main__':
    llist=LinkedList()

    llist.append(2)
    llist.append(10)
    llist.append(6)
    llist.append(7)
    llist.push(4)
    llist.insertAt(4,5)
    # llist.deleteNode(5)
    # print(llist.getCount())
    # llist.iterativeCount()

    # llist.deleteTotalList()
    llist.printlist()
    print("reverse linked list:")
    llist.reverseLinkedList()
    llist.printlist()