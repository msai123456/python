# n=3
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\r")
#
# # using recursion
# def pattern(n):
#     if n==0:
#         return
#     else:
#         pattern(n-1)
#         print("*"*n)

# n=5
# for i in range(n):
#     print("# "*n + "\r")

# for i in range(5):
#     for j in range(5-i):
#         print("*",end="")
#     print("")
# for i in range(4):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("")

# printing the edges
n=5
# for i in range(n):
#     for j in range(n):
#         if (j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(".",end=' ')
#     print("")
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=' ')
#     print()
#
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")
#
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or j==i :
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print("")
#
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")
#
# for i in range(n):
#     for j in range(n):
#         if j==n-1 or i==0 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         if i==0 or j==i or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# # decreasing triangle
#
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# # right angle triangle
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i+1):
#         print("*",end="")
#     print("*")
#
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     for j in range(i+1,n):
#         print("*",end=" ")
#     print("")
#
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n=int(input("enter row"))
# m=int(input("enter col"))
# mat=[]
# for i in range(n):
#     a=[]
#     for j in range(m):
#         a.append(int(input()))
#     mat.append(a)
#
# for i in range(n):
#     for j in range(m):
#         if i==j or j==0 or i==n-1:
#             print(mat[i][j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# n=5
# for i in range(n):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# ////////// palindrom ////////////////
# n=int(input())
# a=n
# sum=0
# while n>0:
#     rev=n%10
#     sum=sum*10+rev
#     n=n//10
#
# if sum ==a:
#     print("this is palindrome")
# else:
#     print("it not palindrome")

# # /// method 2
# n=str(input())
#
# if(n==n[::-1]):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# college problems
# removing duplicate numbeer from list
# def repeat(x):
#     s=len(x)
#     rep=[]
#     for i in range(s):
#         k=i+1
#         for j in range(k,s):
#             if (x[i]==x[j] and x not in rep):
#                 rep.append(x[i])
#     print(rep)
#
# x=[1,2,3,4,4,5,6]
# repeat(x)
#
# n=5
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(2*j-1,end=" ")
#
#     print()

# n=65
# print(chr(n))

# perfect squre
# n=int(input())
# count=0
# for i in range(n):
#     if n==i*i:
#         count+=1
# if count ==1:
#     print("yes")
# else:
#     print("no")
#
# n=2
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#
# print(fact)

# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for i in range(1,i+1):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
