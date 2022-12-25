# it is a linear data structure which works in FIFO first in first out
# operation in queue
# they are seven operation in queue
# creation
# enqueue
# dqueue
# isFull
# isEmptu
# peek
# pop
# in three methods we can create queue
# 1.list with out limit

# class Queue:
#     def __init__(self):
#         self.item=[]
#
#     def __str__(self):
#         values=[str(x) for x in self.item]
#         return " ".join(values)
#
#     # first we need to create isEmpty because this will use in another function
#     def isEmpty(self):
#         if self.item==[]:
#             return True
#         else:
#             return False
#     #ifFull method is wont use in this beacuse it is with out limit list
#     def isFull(self):
#         pass
#
#     # instead of append method we will use enqueue method
#     def enqueue(self,value):
#         self.item.append(value)
#         return "the value is added is sucessuful"
#
#     def dequeue(self):
#         if self.isEmpty():
#             return "there is no element"
#         else:
#             return self.item.pop(0)
#
#     # peek method
#     def Peek(self):
#         if self.isEmpty():
#             return "this is empty queue"
#         else:
#             return self.item[0]
#
#     def delete(self):
#         self.item=[]
#         return "delete sucessfully"
#
#
#
#
# customqueue=Queue()
# customqueue.enqueue(3)
# customqueue.enqueue(5)
# customqueue.enqueue(6)
# customqueue.enqueue(7)
# print(customqueue.dequeue())
# customqueue.delete()
# print(customqueue)


# using linked list using fixed capacity
# for this we need to fixed length

# class queue:
#     def __init__(self,maxvalue):
#         self.item=maxvalue*[None]
#         self.maxvalue=maxvalue
#         self.start=-1
#         self.top=-1
#
#     # for printing result
#     def __str__(self):
#         values=[str(x) for x in self.item]
#         return ' '.join(values)
#
#     def isFull(self):
#         if self.top+1==self.start:
#             return True
#         elif self.start==0 and self.top+1==self.maxvalue:
#             return True
#         else:
#             return False
#
#     def isEmpty(self):
#         if self.top==-1:
#             return True
#         else:
#             return False
#
#     def enqueue(self,value):
#         if self.isFull():
#             return "the queue is full"
#         else:
#             if self.top+1==self.maxvalue:
#                 self.top=0
#             else:
#                 self.top+=1
#                 if self.start==-1:
#                     self.start=0
#             self.item[self.top]=value
#             return "element inserted sucessfully"
#
#     def dequeue(self):
#         if self.isEmpty():
#             return "it is empty"
#         else:
#             fiststelemt=self.item[self.start]
#             start=self.start
#             if self.start==self.top:
#                 self.top=-1
#                 self.start=-1
#             elif self.start+1==self.maxvalue:
#                 self.start=0
#             else:
#                 self.start+=1
#             self.item[start]=None
#             return fiststelemt
#
#     def peek(self):
#         if self.isEmpty():
#             return "it is empty"
#         else:
#             return self.item[self.start]
#
#     def deletes(self):
#         self.item=self.maxvalue*[None]
#         self.top=-1
#         self.start=-1
#
#
#
#
#
# stockqueue=queue(4)
# stockqueue.enqueue(4)
# stockqueue.enqueue(4)
# stockqueue.enqueue(4)
# stockqueue.enqueue(4)
#
# print(stockqueue.dequeue())
# print(stockqueue)
# print(stockqueue.deletes())
# print(stockqueue.peek())

# create queue using linked list
# first we need to assign head and tail value to none

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)


class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        currentn=self.head
        while currentn:
            yield currentn
            currentn=currentn.next

class queue:
    def __init__(self):
        self.linkedlist=Linkedlist()

    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        newnode=Node(value)
        if self.linkedlist.head==None:
            self.linkedlist.head=newnode
            self.linkedlist.tail=newnode
        else:
            self.linkedlist.tail.next=newnode
            self.linkedlist.tail=newnode

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "the queue is empty"
        else:
            tempnode=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
        return tempnode

    def peek(self):
        if self.isEmpty():
            return "no element"
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None


if __name__=="__main__":
    customequeu = queue()
    customequeu.enqueue(3)
    customequeu.enqueue(4)
    print(customequeu)
    print(customequeu.peek())
    customequeu.delete()
    print(customequeu)


# queue model using queue method

