import numpy as no
# kepping two dimensional array
import numpy as np

twoarray=no.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# numppy is library for working with array
# it can also use to with matrix and algebic function

# adding row and column to two dimensional array
# axis =0 (row) and axis =1 (coloumn)

# print("two dimensional")
# newarr=no.insert(teoarry,0,[[2,3,4,5]],axis=1)
# print(newarr[3,3],newarr[1,1])
# traversing two dimensional array
# def travers(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])
# #             it will travel in to every element in the given array
# travers(teoarry)
# ##################### linear search #################
# it will linear search into every element in the given array or list
# def linears(array,value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return "the number is at "+str(i)+" "+str(j)
#     return "the number is not there"
# print(linears(twoarray,8))
# delete element form a array
# newele=np.delete(twoarray,0,axis=0)
# print(newele)
# # the time complexity will be o(mn) because every row and coloum want to move
# mh=np.array([1,2,3,6,3,5],ndmin=5)
# print(mh)
# print(mh.shape)
# reshap
# dim=np.array([1,2,3,4,5,6,7,8,9,9,12,1,1,1,1,1])
# fdim=dim.reshape(4,4)
# print(fdim)
sen=input().split()
print(sen)
rev=sen[::-1]
# for reverse the string
a='.'.join(rev)
print(a)
