# linear search

# def search(arr,n):
#
#     i=0
#
#     while i<len(arr):
#         if arr[i]==n:
#             return "the number is present"
#         i+=1
#     return "not"
#
# arr=[1,2,3,4,5,6,7,8,9]
# n=3
# print(search(arr,n))

# binary search
# all the values should be sorted
# ae will use while using two condition l<u and value shoukd match

def binaryserch(arr,n):
    l=0
    u=len(arr)

    while l<u:
        mid=(l+u)//2

        if arr[mid]==n:
            return True
        elif n>arr[mid]:
            l=mid+1
        else:
            u=mid-1
    return False

arr=[1,2,3,4,5,6,7,8]
print(binaryserch(arr,9))

