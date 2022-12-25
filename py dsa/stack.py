# stack is implemented on first in and last out
# we can implement stack on three types
# 1)list with out size limit
# 2)list with size limit
# 3)linked list

# creation of stack (with out size limit)
# 1)is Empty 2)push 3)pop 4)peek 5)delete

# class Stack:
#     def __init__(self):
#         # want to inital empty list
#         self.list=[]
#     def __str__(self):
#         values=self.list.reverse()
#         values=[str(x) for x in self.list]
#         return '\n'.join(values)
#
#     #1) isEmpty method
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         else:
#             return False
#     #2) push method
#     # it will add in to stack
#     def Pushmethos(self,value):
#         self.list.append(value)
#         return "the element added succesfully"
#
#     #3) pop method in stack
#     # it will remove last element from stack
#     def Pop(self):
#         if self.list is None:
#             return "the stack is empty we cant performe operation"
#         else:
#             self.list.pop()
#
#     # 4)peek method
#     def Peek(self):
#         if self.list is None:
#             return "the stack is empty"
#         else:
#             return self.list[len(self.list)-1]
#         #         it will print the last element in the stack
#
#     # 5)delete method
#     def Delete(self):
#         self.list=None
#
#
#
#
#
# customstack=Stack()
# print(customstack.isEmpty())
# customstack.Pushmethos(1)
# customstack.Pushmethos(2)
# customstack.Pushmethos(3)
# customstack.Pushmethos(4)
# customstack.Pushmethos(5)
# customstack.Pop()
# print(customstack.Peek())
# print(customstack)
# customstack.Delete()
#
# # creating stack with size limit
# this method also same like without limit all methods will include
# 1)isEmpty 2)isFull

# class Stack:
#     def __init__(self,maxvalue):
#         self.maxvalue=maxvalue
#         self.list=[]

#
# beacause of this function string will print
#     def __str__(self):
#         values=self.list.reverse()
#         values=[str(x) for x in self.list]
#         return '\n'.join(values)
#
#
#     # 1)isEmpty
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         else:
#             return False
#     # 2)isFull
#     def isFull(self):
#         if len(self.list)==self.maxvalue:
#             return True
#         else:
#             return False
#     # 3)push method
#     def Push(self,value):
#         if self.isFull():
#             print("Full")
#         else:
#             self.list.append(value)
#             return "the value is sucessfully"
#
#
# mainstack=Stack(1)
# mainstack.Push(3)
# mainstack.Push(4)
# mainstack.Push(4)
# mainstack.Push(5)
#
# print(mainstack)

# creating stack using linked list
#  first step for creating linkedlist we need to create node
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next


class stack:
    def __init__(self):
        self.linkedlist=Linkedlist()

    def __str__(self):
        values=[str(x.value) for x in self.linkedlist]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def Push(self,value):
        node=Node(value)
        node.next=self.linkedlist.head
        self.linkedlist.head=node

    def Ppo(self):
        if self.isEmpty():
            return "it is empty stack"
        else:
            nodevalue=self.linkedlist.head.value
            self.linkedlist.head=self.linkedlist.head.next
            return nodevalue

    def Peek(self):
        if self.isEmpty():
            return "it is empty stack"
        else:
            nodevalue = self.linkedlist.head.value
            return nodevalue

    def delete(self):
        self.linkedlist.head=None



customstacks=stack()
customstacks.Push(2)
customstacks.Push(3)
customstacks.Push(5)
print(customstacks.Peek())
print('----')
print(customstacks)