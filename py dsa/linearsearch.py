# # linear search
# def search(arr,n):
#     i=0
#     while i<len(arr):
#         if arr[i]==n:
#             return True
#         i+=1
#     return False
#
# arr=[3,4,23,12,4,3,23,1]
# n=1
# if search(arr,n):
#     print("found")
# else:
#     print("not fount")

# binary search
# for binary all values should sorted

# pos = -1
#
# def search(list, n):
#     l=0
#     u=len(list)-1
#     while l<=u:
#         mid=(l+u)//2
#         if list[mid]==n:
#             globals()['pos']=mid
#             return True
#         else:
#             if list[mid]<n:
#                 l=mid+1
#             else:
#                 u=mid-1
#     return False
#
#
#
# list = [4,7,8,12,45,99,102,702,10987,56666]
# n = 702
#
# if search(list, n):
#     print("Found at",pos+1)
# else:
#     print("Not Found")

# binary search examples

# def search(det,v):
#     l=0
#     u=len(det)-1
#     while l<=u:
#         mid=(l+u)//2
#         if det[mid]==v:
#             return True
#         else:
#             if det[mid]<v:
#                 l=mid+1
#             else:
#                 u=mid-1
#     return False
#
#
# lt="abcdefghijklmopqrst"
# m=list(lt)
# v="z"
# if search(m,v):
#     print("the item is in")
# else:
#     print("not in the given list")
