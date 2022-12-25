# def recursion(n):
#     if n<1:
#         print("it is less then one")
#     else:
#         recursion(n-1)
#         print(n)
#
# recursion(4)
# example
# def power(n):
#     if n==0:
#         print(1)
#     else:
#         powe=power(n-1)
#         print(powe**2)
# power(9)

# def powerof(n):
#     i=0
#     power=1
#     while i<n:
#         power=power*n
#         i=i+1
#     print(power)
# powerof(3)
#
# print(pow(3,3))
# def resur(n):
#     if n in [0,1]:
#         print(1)
#     else:
#         rec=n*resur(n-1)
#         print(rec)
#
# # resur(4)
# def recursion(n):
#     while n<1:
#         print(n*(n-1))
# recursion(3)

# example recursion fibonacci
#
# def fibonacci(n):
#     assert n>=0 and int(n)==n,"it is not correct number"
#     # first want to set base consdition
#     if n in [0,1]:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# numk=9
#
# if numk<0:
#     print("enter positive number")
# else:
#     for i in range(numk):
#         print(fibonacci(i))

# sum of numbers using recursion
# def sumof(n):
#     # assert is very inportanf
#     assert n>=0 and int(n)==n,"enter the positive number"
#     # the first step is to initilise the case for recursion
#     if n==0:
#         return 0
#     else:
#         return (int(n%10)+sumof(int(n/10)))
# print(sumof(34))
#
# # sum of positive numbers
# def posinum(n):
#     assert n>=0 and int(n)==n,"enter positive number"
#     if n==0:
#         return 0
#     else:
#         return(n+posinum(n-1))
# print(posinum(4))

# power of given numbers

# def powe(base,exp):
#     if exp==0:
#         return 0
#     if exp==1:
#         return base
#     else:
#         return base*powe(base,exp-1)
#
# print(powe(3,4))
# conerting number to binary
# step 1 divide number with 2 and store its reminder
# # step 2 take the quoficent until the it will 0
# def convertb(n):
#     assert int(n)==n,'enter integer'
#     if n==0:
#         return 0
#     else:
#         return n%2+10*convertb(int(n/2))
#
# print(convertb(4))