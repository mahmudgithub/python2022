# creat a simple list method
list=[2,3,4,5,6,7,8,9]
print(list)

mh=[2,3,4,5,6,7,8,9]
print(mh)

#list into list or sub list
list=[2,[3,[4,4,[5,5,5],4],3],3,4,5,6,7,8,9]
print(list)

# find similar cherecter in a list
list=[2,3,4,5,6,7,85,5,5,5,9]
x=list.count(5)
print("similar cherecter in list is:",x)

#find index number in a list
list=[2,3,4,5,6,7,8,9,"mahmud"]
x=list.index("mahmud") # here show mahmud stand position 8
print(x)

#list shorting means small to bigger list
list=[2,3,4,5,6,7,3,8,3,9]
list.sort()
print(list)

list=['a','d','h','m','a','a']
list.sort()
print(list)

list=["mah","ham","mah","azwy"] # for string sorting ,string letter is countable
list.sort()
print(list)

#remove a charecter from list
list=[1,2,3,4,555,6,"mahmud"]
list.remove(list[6]) # here 6 is index number
print(list)

list=[1,2,3,4,555,6,"mahmud"]
list.remove(555) # here 555 is item position
print(list)

#delet last item from list use pop funtion
list=[1,2,3,4,555,6,"mahmud"]
list.pop() # here pop delet last itm
print(list)

#added external element in a list
list=[1,2,3,4,555,6,"mahmud"]
list.insert(7,9) # here 7 is index number and 9 is adding number
print(list)

# 2D list or Matrix
mh=[[1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
   ]
for x in mh:
    for y in x:
        print(y,end=' ') # here end use for new row
    print()



mh=[[1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
   ]
for x in mh:
    for y in x:
        print(y) # if we do not use end statement
    print()


