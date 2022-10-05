#simple only __init__ constructor 
class one:
    def __init__(self,s):
        self.s=s
        print('i am constructor method ')
        print(s)


lol=one('i am constructor parameter')

#simple __init__ constructor method without parameter
class one:
    def __init__(self):
        print('i am constructor method ')

    def fun1(self,x,y):
        self.x=x
        self.y=y
        print(self.x, self.y)

lol=one()
lol.fun1(1,2)

#simple __init__  constructor method with parameter
class one:
    def __init__(self,s):
        self.s=s
        print('i am constructor method ')

    def fun1(self,x,y):
        self.x=x
        self.y=y
        print(x,y, self.s) #self.x ,self.y liki ni karon x,y same method er parameter but self.s liksi>>>
                            #karon s onno method er parameter

lol=one('i am constructor parameter')
lol.fun1(1,2)

#arae claculating by using __init__ 
class one:
    def __init__(self,h,w):
        self.h=h
        self.w=w


    def fun1(self):
        area=.5*self.h*self.w
        print(area)


lol=one(2,3)
lol.fun1()

#__str__ method example
#exaple:1
class one:
    def __st__(self,s):
        self.s=s
        return (s)

lol=one()
print(str('hello'))

#example:2
class one:
    def __init__(self,name):
        self.name=name

    def __str__(self):

        return self.name

lol=one('mahmud')
print(str(lol))

#example:3
class one:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def __str__(self):
        return self.name

lol=one('mahmud',12345)
print(lol)

#simple __repr__ method #
class one:
    def __repr__(self,name,roll):
        self.name=name
        self.roll=roll
        return self.name, self.roll

lol=one()
print(lol.__repr__('mahmud',12345))

#example 2
# simple __init__ and __repr__ method 
class one:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def __repr__(self):
        return self.name, self.roll

lol=one('mahmud',12345)
print(lol.__repr__())

#difference btween __init__,__str__,__repr__ method #
class one:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def __repr__(self):
        return self.name, self.roll

    def  __str__(self):
        return self.name

lol=one('mahmud',12345)
print(lol.__str__())
print(lol.__repr__())


# __repr__ represent __str__ method output
class one:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def __repr__(self):
        return self.name, self.roll

    #def __str__(self):
        #return self.name

lol=one('mahmud',12345)
print(lol.__repr__())
print(lol.__str__())

#Arithmathic  magic method
a=10
b=2
print(a.__add__(b))
print(a.__eq__(b))
print(a.__ne__(b))
print(a.__lt__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__ge__(b))
print(a.__sub__(b))
print(a.__mul__(b))