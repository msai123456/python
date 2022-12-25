class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
        return node

    def insertvalue(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==2:
                newnode.next=None
                self.tail.next=newnode
            else:
                tempnode=self.head
                index=0
                while index<location:
                    tempnode=tempnode.next
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode

    def traversing(self):

        if self.head is None:
            print("the linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node=node.next

    def searching(self,value):
        if self.head is None:
            return "enter linked list"

        node = self.head
        while node is not None:
            if node.value == value:
                return node.value
            node = node.next
        print("the value doess not exist")

    def deleteen(self):
        if self.head is None:
            return "the linked list is empty"
        else:
            self.head=None
            self.tail=None


linkednode=LinkedList()
linkednode.insertvalue(1,2)
linkednode.insertvalue(0,0)
linkednode.insertvalue(2,2)
linkednode.traversing()


print([node.value for node in linkednode])

