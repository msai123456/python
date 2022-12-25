# tree is non linear data structure
# it reverse of the original tree and it has child tree
# 1)implement the tree node

class Treenode:
    def __init__(self,data,child=[]):
        self.data=data
        self.child=child

    def __str__(self,level=0):
        rev=" "*level+str(self.data)+"\n"
        for child in self.child:
            rev+=child.__str__(level+1)
        return rev


    def addNode(self,Treenode):
        self.child.append(Treenode)


tree=Treenode("mains",[])
files1=Treenode('files',[])
files2=Treenode('files1',[])

tree.addNode(files1)
tree.addNode(files2)

subf=Treenode("mk",[])
subf1=Treenode("kl",[])

files1.addNode(subf)
files2.addNode(subf1)
print(tree)
