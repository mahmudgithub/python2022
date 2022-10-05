# simple make a list/array funtion
mhlist=[2,3,4,56,"mahmud",'d']
x=mhlist
print(x)

# find lenght of list
mhlist=[1,2,3,4,5,6,7,8,"mhad",'h']
x=mhlist
print(len(x))

mhlist=[1,2,3,4,5,6,7,8,"mhad",'h']
x=mhlist
print(x,len(x))

#list like a array or position of list element
mhlist=[1,2,3,4,5,6,7,8,"mhad",'h']
x=mhlist
print(x[5])
print(x[8])

# in list funtion we fixed start to end charecter position // its call slicing
mhlist=[1,2,3,4,5,6,7,8,"mhad",'h']
x=mhlist
print(x[3:9]) # 3 call first position and 9 call last position

mhlist=[1,2,3,4,5]
x=mhlist
print(x[2:-2]) # 3 call first position and 9 call last position


mhlist=[1,2,3,4,5,6,7,8,"mhad",'h','d']
x=mhlist
print(x[3:]) # output call 4 to last position

mhlist=[1,2,3,4,5,6,7,8,"mhad",'h','d']
x=mhlist
print(x[:9]) # output call 9 to first position

mhlist=[1,2,3,4,5,6,7,8,"mhad",'h','d']
x=mhlist
print(x[:]) # output call first to last position


# add a int,float,string in list
hlist=["mhad",'h','d']
hlist.append(300)
print(hlist)

hlist=["mhad",'h','d']
hlist.append("mahmud")
print(hlist)

hlist=["mhad",'h','d']
hlist.append('w')
print(hlist)

#add two list
mlist=[1,2,3,4,5,6,7,8]
hlist=["mhad",'h','d']
mlist.extend(hlist)
print(mlist) # give here which list charecter first added

mlist=[1,2,3,4,5,6,7,8]
hlist=["mhad",'h','d']
hlist.extend(mlist)
print(hlist)

#replace spefic list cherecter
hlist=[1,2,3,4,5,6,7,8]
hlist[6]="mahmud" # here 5 replace by mahmud
print(hlist)

# using for loop in a list
mh=[1,2,3,4,5,6,7,8,11,22,444,500]
for x in mh:
 print(x)

mh=[1,2,3,4,5,6,7,8,11,22,444,500]
for x in mh:
 print(mh)

mh=[1,2,3,4,5,6,7,8,11,22,444,500]
for x in range(8):
 print(x)

# find minimum and maximum value from list
mh=[1,2,3,4,5,6,7,8,11,22,444,-500]
x=min(mh)
print(x)

mh=[1,2,3,4,5,6,7,8,11,22,444,-500]
x=max(mh)
print(x)

# sum a list all parameter
mh=[1,2,3,4,5,6,7,8,9]
sum=0
for x in mh:
    print(x)
    sum+=x
print("sum{sum}".format(sum=sum))

# sum a range list funtion
sum=0
for x in range(1,9):
    print(x)
    sum+=x
print("sum{sum}".format(sum=sum))


# ignore and sum string and floting parameter fom a list
mh=[1,2,3,4,5,'mahmud',2.2,5.5]
sum=0
for x in mh:
    if type(x)==int:
     sum+=x
print("sum{sum}".format(sum=sum))


# add a parameter in list in a fixed position
mh=[1,2,3,4,5,6,7,8,9]
mh.insert(4,'mahmud')
print(mh)

# delet a list item
mh=[1,2,3,4,5,6,7,8,9]
del mh[4] # delet one item
print(mh)

mh=[1,2,3,4,5,6,7,8,9]
del mh[0:4] # delet more item
print(mh)

# using pop we can remove  last item and get it outside from a list item
mh=[1,2,3,4,5,6,7,8,9]
x=mh.pop()
print(mh,x) # 1 type
print(mh,"\n",x) # 2 type

# string to list convertion
import re
mh="1,2,3,4,5,6,7,8,9"
x=re.split(',',mh)
print(x)

# list to sentance
mh=["mahmud","is","very","hossain"]
x=' '.join(mh) #here ''. quatation er modde space deya hoy
print(x)

# reverse a list parameter
mh=[1,2,3,4,5,6,8]
mh.reverse()
print(mh)


