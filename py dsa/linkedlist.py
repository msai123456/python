# linked list in python
# it connectionnodes with previous adress
# 1)single linked list
# 2)double linked list
# 3)circular linked list
# 4)double circular linked list

# creation of linkes list
# 1)create head and tail with null
# 2)create a blank node and assign value to it and refernce to null
# 3)link head and tail with these nodes

# advantages of linked list
# 1)no need to pre alocate the space
# 2)insertion is very easy in the linked list

# creating linked list

# it contain two parameter 1)data 2)next both should be assign to none
# and second will head and tail both should contain none
# create class for node
# //////////////////////// method one //////////////////////////////////

# # # in node adress will store from next node
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

    # traversing linked list
    def traversing(self):
        if self.head is None:
            print("enter linked list")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next

    #   searching valur in linked list
    def searching(self,nodevalue):
        if self.head is None:
            return "enter linked list"

        node=self.head
        while node is not None:
            if node.value == nodevalue:
                return node.value
            node=node.next
        print("the value doess not exist")

    # delete entire linked list
    def entirelist(self):
        if self.head is None:
            print("the head is empty")
        else:
            self.head=None
            self.tail=None
    def deletion(self,location):
        if self.head is None:
            print("the liked list is empty")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
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




singlelist=Linklist()
singlelist.insert_list(1,1)
singlelist.insert_list(23,1)
singlelist.insert_list(32,0)
singlelist.insert_list(90,1)
singlelist.searching(1)
print([node.value for node in singlelist])

# singlelist.deletion(3)
# print([node.value for node in singlelist])
# singlelist.traversing()

# print(singlelist.searching(5))
# singlelist.entirelist()
# print([node.value for node in singlelist])

# ////////////////////////////// method two ////////////////////////////////////////////
#
# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next
#
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#
#     def print(self):
#         if self.head is None:
#             print("enter the value")
#             return
#         itr=self.head
#         list=' '
#
#         while itr:
#             list+=str(itr.data)+"--->" if itr.next else str(itr.data)
#             itr=itr.next
#         print(list)
# ll=Linkedlist()
# ll.head=Node(2)
# ll.print()
# ll.head=Node(3)
# ll.print()
