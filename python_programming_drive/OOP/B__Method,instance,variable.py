#difference ,method er bire parameter define and vetore parameter define kora

#when prameter define outer  method
class Student:

    def one(self):
        print(self.name)
        print(self.roll)

lol=Student()
lol.name='mahmud'
lol.roll=12345
lol.one()
sos=Student()

sos.name='lamyaa'
sos.roll=000
sos.one()


#when parameter define enter method
class one:
    def fun(self,x,y):
        self.x=x
        self.y=y

        print(x ,y)

lol=one()
lol.fun(2,5)

#user login,logout related class
class user:

    def login(self):
        email=input('enter your email: ')
        password=input('enter your password: ')
        if email==self.email and password==self.password:
            login=True
            print('login successful')
        else:
            print('failed to login')

    def logout(self):
        login=False
        print('logout')

    def isloggedin(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.isloggedin():
            print(self.name)
        else:
            print('user is not logged')

lol=user()
lol.name='mahmud'
lol.email='mahmud@gmail.com'
lol.password='2580'
lol.login()


#difference btween self and not self joint parameter
class one:
    name=''
    woner=''
    def fun(self):
        print(self.name ,'and ' ,self.woner)

    def fun2(self,address):
        print(self.name, self.woner)
        print(address)

lol=one()
lol.name='mahmud'  #indirectly define value first then function call
lol.woner='hossain'
lol.fun()

lol.fun2('raj') #directly value send in funtion

# __init__ method er use 
class One:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('i am init funytiuon')


    def fun(self):

        print(self.x)
        print(self.y)


lol=One('mahmud',12345)
lol.fun()


#__init__ class inherate korte super method use korte hobe 
class one:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('i am init funytiuon')


    def fun(self):

        print(self.x)
        print(self.y)

        
class two(one):
    def __init__(self,x,y):
        super().__init__(x,y)

    def fun2(self):
        print(self.x + self.y)

lol=two(2,3)
lol.fun2()

#multiple inheritance by using init method 
class one:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('i am init method')


    def fun1(self):

        print('sum: ', self.x+self.y)

class two(one):
    def __init__(self,x,y):
        super().__init__(x,y)

    def fun2(self):
        print('sub: ', self.x - self.y)

class three:
    def fun3(self,x,y):
        print('divion: ', x/y)

class four(two,three):
    def __init__(self,x,y):
        super().__init__(x,y)


    def fun4(self):
        print('multi: ',self.x*self.y)



lol=four(2,3)
lol.fun1()
lol.fun2()
lol.fun3(10,5)
lol.fun4()

#funtion/method overrinding example 
class a:
    def fun1(self,x,y):
        self.x=x
        self.y=y
        print(self.x + self.y)

class b(a):
    def fun2(self):
        print(self.x+self.y+100)  #overrining 

class c(b):
    def fun3(self):
        print(self.x+self.y+000) #overriding 

lol=a()
lol=b()
lol=c()
lol.fun1(1,1)
lol.fun2()
lol.fun3()

#method overloadig example but python doesnot support method overloading 
class a:
    def fun1(self,x,y):
        self.x=x
        self.y=y
        print(self.x + self.y)

class b(a):
    def fun2(self,z):
        print(self.x+self.y+z)  #overloading 

lol=a()
lol=b()
lol.fun1(1,1)
lol.fun2()


#different type of variable (class variable, instance variable)
class student:
    name='mahmud' #class variable ,ja thod er bire but class er uder a define kora hoy
    roll=12345

    def fun(self,x,y):
        self.x=x # instance variable ,ja method er vetore define kora hoy and object er sate related
        self.y=y
        print(self.x,self.y) #instance variable call by self.variable name
        print(student.name)  #class variable call by class name.variable name

lol=student()
lol.fun(123,456)

#different type of methods (class method, instance method, static method)
class student:
    name='mahmud' #classs variable 

    def fun(self,x,y): #its a instance method 
        self.x=x     #instance variable 
        self.y=y
        print(x,y)

    def fun2(self,z): #its a anotjer instance method 
        self.z=z
        print(z)

    @classmethod #its class method and class method use decorator 
    def fun3(cls):
        print(cls.name)


lol=student()  #object
lol.fun(0,1)
lol.fun2(2)
lol.fun3()
#example2:
class student:
    name='mahmud' #classs variable 

    def fun(self,x,y): #its a instance method 
        self.x=x     #instance variable 
        self.y=y
        print(self.x,self.y)
        print(student.name) #class variable call by class name.variable self.name


    def fun2(self,z): #its a anotjer instance method 
        self.z=z
        print(z)

    @classmethod #its class method and class method use decorator 
    def fun3(cls):
        print(cls.name)

class teacher(student):
    city='raj'

    def fun4(self):
        pass
    @classmethod
    def fun5(cls):
        print(cls.city)


lol=student()  #object
lol=teacher()
lol.fun(0,1)
lol.fun2(2)
lol.fun3()
lol.fun4() 
lol.fun5()

#staticmethod example gulo compire korley buja ji,jodi self use na korte chi tobe @staticmethod use
class lol: #this class show error ,cause instance method er vetore self use kori
    def fun():
        print('mahmud')
sos=lol()
sos.fun()

class lol: #this class perface ,cause self use koresi
    def fun(self):
        print('mahmud')
sos=lol()
sos.fun()

#jodi method er vetore self use na korte chi tobe @staticmethod likte hoy method er upore
class lol:
    @staticmethod
    def fun():
        print('mahmud')
sos=lol()
sos.fun()

#another example of static method
class lol:
    @staticmethod
    def fun(x,y):
        print()
sos=lol()
lol.fun(1,2)

#show class variable,instance variable,class method,instance method,static method in one program
class one:
    name='i am classmethod'  #class variable

    def fun(self,x,y):  #instance method
        self.x=x     #instance variable
        self.y=y     #instance variable
        print(x+y)

    @classmethod  #class method
    def fun1(cls):
        print(cls.name)

    @staticmethod  #static method
    def fun2():
        print('i am staticmethod')

lol=one()
lol.fun(2,2)
lol.fun1()
lol.fun2()

#simple constructor method
class one:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        print(name,roll)

lol=one('mahmud',12345)

#class method Without parameter example
class one:
    x='hello world'
    @classmethod
    def fun(cls):
        print(cls.x)

lol=one()
lol.fun()

#class method With parameter example
class one:
    x='hello'
    @classmethod
    def fun(cls,y):            #same as self,y
        cls.y=y                #self.y=y
        print(cls.x, cls.y)    #print(self.y)

lol=one()
lol.fun(123)

