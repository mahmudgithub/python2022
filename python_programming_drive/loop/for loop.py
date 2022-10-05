mh=[1,2,3,4.5,6,7,8,9,0]
for x in mh:
 print(x)

box1 = ["red", "big", "tasty"]
box2 = ["apple", "banana", "cherry"]
 for x in box1:
 for y in box2:
 print(x, y)


for x in range(9):
  print(x)


for x in range(9):
  print(x)
else:
  print("Finally finished!")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
   continue
  print(x)


for x in "banana":
  print(x)


  for a in range(9):
      print(a+1)

#python for loop funtion
x=[1,2,3,4,5,6,7]
for i in(x): # pritn a list data
    print(i)


for i in range(10,12): # use limit where to where output print
    print(i)


for i in range(3,15,3): # incrise number 3
    print(i)


for i in range(30,15,-3): # decrise number -3
    print(i)

# for loop with else funtion
mh=[1,2,3,4,5]
for x in range(1,5):
  print(x)
else:
    print("final value:",x)

# use enumerate funtion in for loop to give serial number
mh=[1,2,3,4,5,"mahmud",'h']
for x, y in enumerate(mh):
  print(x,y)

#use break in for loop
for x in range(12):
    if(x>6):
     break
    print(x)

#using for loop find even and odd number
for x in range(1,100):
    if(x%2==0): # for even number
        print(x)

        for x in range(1, 100):
            if (x % 2 == 1): # for odd number
                print(x)

# use "and" funtion in for loop

for x in range(1,100): # use range method
 if(x%2==0 and x%6==0):
    print("devided",x)
else:
    print("no devided",x)



    mh=[10,20,40,50,60,65,70,71,73,67,95,43] # use list method
    for x in mh:
        if (x % 2 == 0 and x % 5 == 0):
            print("devided", x)
    else:
     print("no devided", x)

# use "or" funtion in for loop

for x in range(1,100): # use range method
 if(x%2==0 or x%6==0):
    print("devided",x)
else:
    print("no devided",x)



    mh=[10,20,40,50,60,65,70,71,73,67,95,43] # use list method
    for x in mh:
        if (x % 2 == 0 or x % 5 == 0):
            print("devided", x)
    else:
     print("no devided", x)

mh=[1,2,3,4,5,6,7,8,9]
min=mh

# sum all parameter from a range using for loop
sum=0
for x in range(1,11):
    print(x)
    sum+=x
print("sum{sum}".format(sum=sum))
