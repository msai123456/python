# it is collections of key and value pair
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////// it will work on hashing function (dictionary) ///////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# it is unorder,changeble,indexed
# /////////////////// methods ////////////////////////
# 1.pop() 2.popitems 3.update.() 4.value() 5.value() 6)fromvalue() 7.fromkeys()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////operators in dict ////////////////
# 1) in operator for checking present or not /return boolen value
# 2) in dict.values for checking values // it will take O(1) time complexity because dict will run hash function
# 3) for operator for traversing in the entire the dict
# 4) all() operator it will return the boolean value based on their condition
# 5)any() any operator any one will be enough
# 6)sorted() method

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

dictionarie={
    'name':"sucharith",
    'age':20,
    'class':14,
    "place":'chennai'
}

# /////////////in operators/////////////////////////
print("age" in dictionarie)
print(22 in dictionarie.values())
# /////////////all operators/////////////////////////
print('all')
mysdi={1:'',2:False}
print(all(mysdi))

# print(dictionarie)
# # updating the values in dictionre
# dictionarie['age']=90
# print(dictionarie)
# # adding element to dict
# # it will add to end of the dict
# dictionarie['height']=123
# print(dictionarie)
# traversing the dict
# for i in dictionarie:
#     if i =="name":
#         print("the is there in the given key")
#         print(i+":"+dictionarie[i])

# searching

# def search(sic,valu):
#     for i in sic:
#         if i == valu:
#             print("the key is present")
#             print(i,sic[i])
#         else:
#             print("key not available")
#             break
# search(dictionarie,'j')

# def search(src,value):
#     for key in src:
#         if src[key]==value:
#             return key,value
#     return "the value is not present"
# search(dictionarie,20)
# deleting element form dict
# print(dictionarie.popitem())
# print(dictionarie)
# fromkey() method///////////////
# it will creat the different keys with same value
# mydict={}.fromkeys([1,2,43,4,9],0)
# # print(mydict)
# print(dictionarie.items())
# print(dictionarie.setdefault('lion',123))
# print(dictionarie)

# update method
mynew={1:2,2:3,9:0}
mynew.update(dictionarie)
dictionarie.update(mynew)

print(mynew)
print(dictionarie)