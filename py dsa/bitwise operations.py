# BITWISE OPERATIONS
#in bit wise operations will work on only in bits

# "and" operator in python
# 1) first it will convert the number in to binary then it will perform the operation
# 2) based on the given operation input it will perform

# example
#  10 will represent in binary   1010
#  9 will represent in binary    1001
# it will perform and operation  1000 (output will be 8)
a=10
b=9
c=a&b
print("and operaion",c)

# "or" operation
# 4 in binary 0100
# 5 in binary 0101
# output will be 0101(5)
n=4
m=5
print("or operation",n|m)

# "xor" operations
# in xor only one input should be 1,if both given as 1 it will give 0
# 4 in binary 0100
# 5 in binary 0101
# output will be 0001(1)
print("xor operation",n^m)



#decimal to binary by using while
n=9
while n>=1:
    print(n%2,end="")
    n=n//2



