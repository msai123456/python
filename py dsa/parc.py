# linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
# creating linked list
class Linklist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insert_list(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                # assigning next value from head
                newnode.next=self.head
                self.head=newnode
            elif location == 1:
                # for last node next will none
                newnode.next=None
                # for creating before next is newnode
                self.tail.next=newnode
            else:
                tempnose=self.head
                index=0
                while index < location -1:
                    tempnose=tempnose.next
                    index+=1
                nextnode=tempnose.next
                tempnose.next=newnode
                newnode.next=nextnode
    def search(self,value):
        if self.head is None:
            return "node is empty"
        node=self.head
        while node is not None:
            if node.value==value:
                return node.value
            node=node.next
        print("the node does not exist")
    def deleteall(self):
        if self.head is None:
            return "the list is empty"
        else:
            self.head=None
            self.tail=None

    # delete particular value
    def deletpa(self,location):
        if self.head is None:
            return "the list is none"
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head= self.head.next
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=None
    def deletenode(self,value):
        temps=self.head
        if (temps is not None):
            if temps.value==value:
                temps=temps.next
                # self.head=temps.next
                temps=None
        while(temps is not None):
            if temps.value==value:
                break
            prev=temps
            temps=temps.next
        prev.next = temps.next
        temps = None






custome=Linklist()
custome.insert_list(1,0)
custome.insert_list(2,0)
custome.insert_list(3,0)
custome.insert_list(4,0)

print([node.value for node in custome])
custome.deletenode(2)
print([node.value for node in custome])
