# python lists
# list is collects of items and changeble ,orderded,duplicate
# it will creat in []
# it will allow all type of data types
# items=['name',34,39.4,4,67,"regnum",9,23,45]
# print(items)
# # accessing list items
# print(items[2])
# # range function will use to finding range
# for i in range(len(items)):
#     print(i)
# update and insert the list
# upade list
# items[0]="names"
# it will mutate the given list
# print(items)
# # insert the are four methods
# # 1)insert 2)append 3)extend
# items.insert(0,'kijg')
# # print(items)
# # append add the element the last position
# items.append(89)
# # print(items)
# # extend it will join the two lists
# newlist=[23,'sai',12,45]
# items.append(newlist)
# print(items)
# slice the element
# items=['name',34,39.4,4,67,"regnum",9,23,45]
# print(items[2:5])
# print(items[::-1])
# # delete()
# del items[2]
# print(items)
# # we can use slice method also for deleting
# del items[1:5]
# print(items)
# # using IN operator in list
# items=['name',34,39.4,4,67,"regnum",9,23,45]
# if 34 in items:
#     print(items.index(34))
# else:
#     print("the number is not there in list")
# example
# mylist=list()
# while(True):
#     inp=(input("enter number"))
#     if inp=="done": break
#     value=float(inp)
#     mylist.append(value)
# ave=sum(mylist)/len(mylist)
# print("average value",ave)
# project on array/list
# nod=int(input("how many days temperature you want?"))
# total=0
# temp=[]
# for i in range(nod):
#     n=int(input("enter the "+str(i+1)+"temperature"))
#     temp.append(n)
#     total+=temp[i]
# avg=round(total/n,2)
# print(avg)
#
# above=0
# for j in temp:
#     if j>avg:
#         above+=1
# print("the above days is"+str(above))

x = int(input())
y = int(input())
z = int(input())
n = int(input())
output = [];
abc = [];
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                abc = [X,Y,Z];
                output.append(abc);
print(output);
