# creation of binary tree using linked list

#
# # pre order
import queue as que
class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


newbt=Treenode("Drinks")
left=Treenode("hot")
tea=Treenode("tea")
coffe=Treenode("coffee")
left.left=tea
left.right=coffe
right=Treenode("cool")
alcoholic=Treenode("alcoholic")
nonclchohlic=Treenode("non-alcoholic")
right.left=alcoholic
right.right=nonclchohlic

newbt.left=left
newbt.right=right

def preorder(rootnode):
    if rootnode == None:
        return
    print(rootnode.data)
    preorder(rootnode.left)
    preorder(rootnode.right)
print("////////////////////preorder//////////////////////")
preorder(newbt)

def inorder(rootnode):
    if rootnode == None:
        return
    inorder(rootnode.left)
    print(rootnode.data)
    inorder(rootnode.right)

print("////////////////////inorder//////////////////////")
inorder(newbt)

def postorder(rootnode):
    if rootnode == None:
        return
    postorder(rootnode.left)
    postorder(rootnode.right)
    print(rootnode.data)

print("////////////////////postorder//////////////////////")
postorder(newbt)

# ///////////////level order traversal /////////////////
# it is also called breadth first search

# def levelorder(rootnode):
#     if not rootnode:
#         return
#      else:
#         customequeue=que.queue()
#         customequeue.enqueue(rootnode)
#         while not(customequeue.isEmpty()):
#             root=customequeue.dequeue()
#             print(str(root))
#             if(root.value.left is not None):
#                 customequeue.enqueue(root.value.left)
#             if(root.value.right is not None):
#                 customequeue.enqueue(root.value.right)
# print("/////level order///////")
# levelorder(newbt)


# create binary tree using list(array)
