# def add(a,d):
#     return a+d
#
# print(add(2,3))
# # creating class
# class sau():
#     def __init__(self,name,sur):
#         self.name=name
#         self.sur=sur
#
#
# bhu=sau('sai','sucharith')
# print(bhu.name)
#
# joi=sau("leo","alek")
# traversing it is nothing but going every element in given array

# l=[2,3,4,5]
# for i in l:
#     print(i)
# searching array
# arr=[3,9,1,3,4,3,0,2]
# def search(array,els):
#     for i in array:
#         if els==i:
#             return array.index(els)
#     return "the element is not present in the given list"
# print(search(arr,4))
# for deleting element from array
# arr=[1,2,3,4,5,6]
# arr.remove(5)
# print(arr)
# creating two dimension array
# import numpy as np
# teoarry=np.array([7,9,8,8],[8,9,0,6],[9,8,6,7])
# print(teoarry[1][0])


# class dogs:
#     def __init__(self,name,breed):
#         # __init__ will constructer when class will call
#         self.name=name
#         self.breed=breed
#     def calling(gfsd):
#         print("the breed is "+gfsd.breed+"\nname is:"+gfsd.name)
#
# p1=dogs("tony","gt")
# p1.calling()
# find the missing number in array
# arr=[1,2,3,4,5,6,8]
# ent=len(arr)
# def missingn(myarr,n):
#     total= (n + 1)*(n + 2)/2
#     sumlo=sum(arr)
#     print(total-sumlo)
# missingn(arr,ent)

# ni=int(input("enter numbers"))
# sums=0
# for i in range(ni+1):
#     sums+=i
# print(sums)
# find the max in given array/////////////////////////////////////
# a=[2,4,5,7,9,12,18,19,25,46,12]
# def maxmul(arras):
#     multitotal = 0
#     for i in range(len(arras)):
#         for j in range(i+1,len(arras)):
#             if arras[i]*arras[j]>multitotal:
#                 multitotal=arras[i]*arras[j]
#                 pairs=str(arras[i])+","+str(arras[j])
#     print(pairs)
#     print(multitotal)
#
# maxmul(a)
# checing a uniq list or not/////////////////////////////////////////////

# a=[1,2,4,5,2,8,9,20,90,89,68,56,45]
# def checklist(arr):
#     dar=[]
#     for i in arr:
#         if i in dar:
#             print(i)
#             return False
#         else:
#             dar.append(i)
#     return True
# print(checklist(a))

#  check wheather the given two lists is perumutations or nor
#
# def perrumuta(list1,list2):
#     if len(list1)!=len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1==list2:
#         return True
#     else:
#         return False
# #     it want to check two conditions length and the given elements also
# list1=[1,2,3,5]
# list2=[4,3,2,1]
# print(perrumuta(list1,list2))
# rotate matrix
