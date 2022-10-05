#....................using simple class

class user:
    name=''
    email=''
    password=''
    login=True

    def login(self):
        email=input('enter your email:')
        password=input('enter your password:')

        if email==self.email and password==self.password:
            login=True
            print('login successful')
        else:
            print('login fail')
    def logout(self):
        login=False
        print('logout')
    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedIn():
            print(self.name,"/", self.email)
        else:
            print('user is not valied')
user1=user()
user1.name='mahmud'
user1.email='mahmudhossain835@gmail.com'
user1.password='2580'

user1.login()
user1.profile()
hello=input()

#......................using constructor
class user:
    name=''
    email=''
    password=''
    login=True

    def __init__ (self,name,email,password):
        self.email=email
        self.name=name
        self.password=password



    def login(self):
        email=input('enter your email:')
        password=input('enter your password:')

        if email==self.email and password==self.password:
            login=True
            print('login successful')
        else:
            print('login fail')
    def logout(self):
        login=False
        print('logout')
    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedIn():
            print(self.name,"/", self.email)
        else:
            print('user is not valied')
user1=user('mahmud','mahmudhossain835@gmail.com','2580')

user1.login()
user1.profile()
hello=input()



#.................................
class lol:
    name=''
    roll=''
    city=''
    def fun1(self):
        print('hi i am ',self.name,'roll is ',self.roll)
    def fun2(self,city):
        print('my city is:',city)
s=lol()
s.name='lamyaa'
s.roll=1222
s.fun1()
s.fun2('pabna')

#............................
class calculator:
    def sum(self,a,b):
        print('sum is:',a+b)
    def sub(self,a,b):
        print('sub is:',a-b)
    def mul(self,a,b):
        print('mul is:',a*b)
    def div(self,a,b):
        try:
            print('div is:',a/b)
        except Exception as e:
            print(e)

lol=calculator()
lol.sum(2,2)
lol.sub(5,2)
lol.mul(2,2)
lol.div(5,0)

#.............................
class test:
    def __init__(self):
        print('i am constuctor')
    def fun1(self):
        print('i am funtion one')
    def fun2(self):
        print('i am funtion 2')
lol=test()
#lol.fun1()
lol.fun2()

#...............................multiple construtor call
class Hello:
    def __init__(self):
        print ("Constractor")

    def sayHello(self):
        print ("Hello world!")

hello1 = Hello()
hello1.sayHello()

hello2 = Hello()
hello2.sayHello()

#................
class math:
    def __init__(self,x,y):
        print('sum:',x+y)
lol=math(2,3)

class math:
    def __init__(self,x,y):
        print('sum:',x+y)

class math2(math):
    def __init__(self,a,b):
        print('sub:',a-b)

lol=math(2,3)
gol=math2(5,2)
gol=math(2,2)

#.....................
import math

class lol:
    def __init__(self,n):
        print('result:',math.tan(n))

x=lol(45)

#...........................
class person:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
        print('my bio:',name,age,roll)

lol=person('mahmud',25,12020)

#.......................
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print('hello '+self.name)

lol=Person('mahmud',23)
lol.fun()

#............................change any part
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print('hello '+self.name)

lol=Person('mahmud',23)
lol.name='hossain'
lol.fun()

#..........................
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print('hello '+self.name)

lol=Person('mahmud',23)
lol.name='hossain'
lol.fun()


class lol:

    def fun(self,x,y):
        print("function one",x+y)
    

    def __init__(self):
        print("inin function")

    

    def fun2(self):
        print("function two")
hi=lol()
hi.fun2()
hi.fun(1 ,2)


class lol:
    name=''
    roll=''
    def __init__(self,x,y):
        self.x=name
        self.roll=roll

s=lol('mahmud',133)

class lol:
    def __init__(self,cool):
        self.n=cool

    def fun(self):
        print("hell"+self.n)
x=lol("mahmjd")
x.fun()

class lol:
    def __init__(self,x):
        self.n=x
    def fun(self):
        print(self.n*self.n)
s=lol(2)
s.fun(3)

import math
class lol:
    def __init__(self,x):
        self.n=x
    def fun(self):
        print(self.n*self.n)
class col(lol):
    def fun2(self):
        print(math.sin(self.n))
s=col(90)
s.fun2()

class lol:
    def sum(self,x,y):
        print("reslt sum:",x+y)
    def sub(self,x,y):
        print("result sub:",x-y)
    def div(self,x,y):
        print("result dive:",x/y)
s=lol()
s.sum(2,2)
s.sub(7,3)
s.div(12,3)

#not working function
class lol:
    def __init__(self,x,y):
        print("sum:",x+y)
    def __init__(self,x,y):
        print("sub:",x-y)
s=lol(2,2)

#above function modefy
class lol:
    def __init__(self,x,y):
        print("sum:",x+y)
s=lol(2,2)

#use init and def with in same class value
class lol:
    def __init__(self,x,y):
        self.a=x
        self.b=y

    def sum(self):
        print("sum is: ",self.a+self.b)

    def sub(self):
        print("sub is: ",self.a-self.b)
s=lol(2,2)
s.sum()
s.sub()


class lol:
    def __init__(self,x,y):
        print("hello math")
        self.r=x
        self.r=y
    def fun(self):
        print("sum is:",self.r+self.r)
s=lol(2,2)
s.fun()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(self.name)
    print(self.age)


p1 = Person("John", 36)
print(p1.name)


#use of __init__ funtion
class lol:

   # name=''
   # roll=''
    #city=''

    
    def __init__(self,name,roll,city):
        self.name=name
        self.roll=roll
        self.city=city
        
        print("i am constructor, so run must")

    def fun(self):
        print("i am",self.name,"and my city is",self.city)

    def fun2(self):
        print("my roll is",self.roll)

sos=lol('mm','123','raj')

sos.fun()

#The str() function is used here to convert the age attribute, which is an integer, to a string,
# so you can use it in the print() function.
class Dog:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")


    def birthday(self):
        self.age +=1


ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

ozzy.doginfo()
skippy.doginfo()
filou.doginfo()


#Python Multiple Inheritance
class one:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

class two():
    def __init__(self,city,country):
        self.city=city
        self.country=country


class three(one,two):
    def __init__(self,name,roll,city,country,board):
        self.board=board

        one.__init__(self,name,roll)
        two.__init__(self,city,country)
        print("my name:",name,"my roll:",roll,"my city:",city,"my country:",country,"board is:",board)

sos=three("mahmud,",1234,"rajshahi,","bagladesh,","dhaka")

#Python Multi-level Inheritance Example
class one:
    def fun1(self):
        print("first class")


class two(one):
    name=""

    def fun2(self):
        self.name=name
        print(self.name)

class three(one):
    roll=''
    def fun3(self):
        self.roll=roll
        print(self.roll)
        

class four(two,three):
    def fun4(self):
        print(self.name)
        print(self.roll)




sos=four()
sos.name="mahmud"
sos.roll=1234

#sos.fun1()
#sos.fun2()
#sos.fun3()
sos.fun4()

#