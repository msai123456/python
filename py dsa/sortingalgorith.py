# bubble sort
# def sort(nums):
#     size=len(nums)
#     for i in range(size-1):
#         swapped=False
#         for j in range(size-1-i):
#
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=nums[j+1]
#                 nums[j+1]=temp
#                 swapped=True
#         if not swapped:
#             break
#     return(nums)

# nums=[9,3,4,23,2,1]
# nums1=["sai","sucharith","alex"]
# print(sort(nums))

# excer

# def sort(element,key=None):
#     size=len(element)
#     for i in range(size-1):
#         swapped=False
#         for j in range(size-1):
#             a = element[j][key]
#             b = element[j + 1][key]
#             if a>b:
#                 temp=element[j]
#                 element[j]=element[j+1]
#                 element[j+1]=temp
#                 swapped=True
#         if not swapped:
#             break
#
# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
#
# sort(elements,key="transaction_amount")
# print(elements)

# selection sort

# def sorte(arr):
#     for i in range(len(arr)-1):
#         min_pos=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min_pos]:
#                 min_pos=j
#         arr[i],arr[min_pos]=arr[min_pos],arr[i]
#     return arr
#
#
# arr=[5,4,3,2,1,0]
# print(sorte(arr))


# # insertion sorting
#
# def insert_sort(arr):
#     size=len(arr)
#     for i in range(size):
#         while arr[i-1]>arr[i] and i>0:
#             arr[i],arr[i-1]=arr[i-1],arr[i]
#             i-=1
#
#     return arr
#
# arr=[9,5,7,6,4,3,2,1,0,7,4]
# print(insert_sort(arr))

# merge sort
# first it will divide entire elements and merge according to the element
# and it will take time comlexity O(nlogn)
# it will divide and conqure alogorith
# it will divide array in to
# 1)split array into half
# 2)call the merge sort on the both array until sort them recursively
# 3)combined two splited array into one array

def merge_sort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
                k+=1
            else:
                arr[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr


arr=[9,8,7,6,5,1000,12,34,3,2,1]
print(merge_sort(arr))

print(dir())

# quick sort










