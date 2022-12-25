# class Node:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
#
# class circularlinked:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#
#     def __iter__(self):
#         node=self.head
#
#         while node:
#             yield node
#             node=node.next
#             if node==self.tail.next:
#                 break
#
#     def create_cli(self,value):
#         node=Node(value)
#         node.next=node
#         self.head=node
#         self.tail=node
#         return "the cli has created"
#     def insertion_cli(self,Nodevalue,location):
#
#         if self.head is None:
#             return "the cli is empty"
#         else:
#             newNode = Node(Nodevalue)
#             if location=="f":
#                 newNode.next=self.head
#                 self.head=newNode
#                 self.tail.next=newNode
#             elif location=="l":
#                 newNode.next=self.tail.next
#                 self.tail.next=newNode
#                 self.tail=newNode
#             else:
#                 tempNode=self.head
#                 index=0
#                 while index<location-1:
#                     tempNode=tempNode.next
#                     index+=1
#                 currentNode=tempNode.next
#                 tempNode.next=newNode
#                 newNode.next=currentNode
#             return "the node has optined"
#
#     def traversel(self):
#         if self.head is None:
#             return "the cli is empty"
#         else:
#             tempnode=self.head
#             while tempnode:
#                 print(tempnode.data,end=" ")
#                 tempnode = tempnode.next
#                 if tempnode == self.tail.next:
#                     break
#
#     def searchind(self,fvalue):
#         if self.head is None:
#             return "there is not any value"
#         else:
#             tempnode=self.head
#             while tempnode:
#                 if tempnode.data == fvalue:
#                     return tempnode.data
#                 tempnode=tempnode.next
#
#                 if tempnode == self.tail.next:
#                     return "node not exist"
#
#
# circularli=circularlinked()
# circularli.create_cli(10)
# circularli.insertion_cli(1,"l")
# circularli.insertion_cli(2,1)
# circularli.insertion_cli(0,2)
# print(circularli.searchind(1))
# print(circularli.traversel())
# print([node.data for node in circularli])

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class circular:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next

    def insertNode(self,value):
        node=Node(value)
        node.next=node
        self.head=node
        self.tail=node

    def insertCSLL(self,value,position):
        if self.head is None:
            print("the clli is empty")
        else:
            newnode = Node(value)
            if position=='F':
                newnode.next=self.head
                self.head=newnode
                self.tail.next=newnode
            elif position=='E':
                newnode.next=self.tail.next
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0

                while index<position-1:
                    tempnode=tempnode.next
                    index+=1
                nextvalue=tempnode.next
                tempnode.next=newnode
                newnode.next=nextvalue




cirlinkes=circular()
cirlinkes.insertNode(1)
cirlinkes.insertCSLL(2,'F')
cirlinkes.insertCSLL(3,'E')
cirlinkes.insertCSLL(0,'F')
cirlinkes.insertCSLL(2,2)
cirlinkes.insertCSLL(2.1,3)
cirlinkes.insertCSLL(4,5)
cirlinkes.insertCSLL(5,6)
print([node.data for node in cirlinkes])