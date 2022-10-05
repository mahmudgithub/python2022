#user key board input with if,elif function 
def fun(x,y):
    if x>y:
        return ('x is bigger then y is: ',x-y)
    elif x<y:
        return ('y is bigger then x is:',y-x)
    else:
        return 'both are equal'

lol=int(input('enter value of x:'))
sos=int(input('enter value of y:'))
print(fun(lol,sos))

#user key board input with if,elif and fomated function 
def fun(x,y):
    if x>y:
        return  x
    elif x<y:
        return y
    else:
        return 'both are equal'

lol=int(input('enter value of x:'))
sos=int(input('enter value of y:'))
hi=fun(lol,sos)
print(f"{hi} is bigger")

