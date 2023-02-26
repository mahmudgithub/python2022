# def fun():
#     print("Allahu akbar")
# fun()

# def fun(name):
#     print("my name is "+name+" from rajshahi")
# fun("mahmud")
# s=fun
# s("hossain")

# def fun(first,second):
#     print("i am "+first+" he is "+second)
# s=fun
# s("mahmud","nannu")
# s("hossain","nannu")

# def fun(value):
#     if value<5:
#         return value
#     else:
#         return value
# print(fun(2))
# print(fun(-10))

# def person(name,age,country):
#     print(name,age,country,sep=" / ")
# person("mahmud",28,"Bangladesh")

# def fun(mh):
#     print("name:{mh}".format(mh=mh))
# fun("Mahmud")


# def fun(name,age,city):
#     print("my name is: "+name+" age is: "+age+" city is: "+city,sep="!")
# fun(name="mahmud",age=str(26),city="Rajshahi")
# fun("hossain",str(30),"dhaka")
# fun(name="nannu",city="khulna")


# def fun(age,city,name="mahmud"):
#     print("may name is:"+name+" my age is :"+age+"my city is :"+city)
# fun("six","dhaka")
# fun("mahmud","hossain","nannu")


# class student:
#     def one(self):
#         print(self.name)
#         print(self.age)
# lol=student()
# lol.name="mahmud"
# lol.age=26
# lol.one()

# sos=student()
# sos.name="hossain"
# sos.age=28

# class one:
#     def fun(self):
#         print("ALLALHU AKBER")
#     def fun1(self):
#         print("O ALLAH PLEASE FORGIVEN ME")
#     def fun2(c):
#         print("may allah you know everthing of my heart")
# sos=one()
# sos.fun()
# sos.fun1()
# sos.fun2()


# class student:
#     def one(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#         print(name,age,city)

# sos=student()
# sos.one("mahmud",28,"Rajshahi") 

# class student:
#     def one(self,name,roll):
#         print(name,roll)

#     def two(self,name,roll):
#         self.name=name
#         self.roll=roll
#         print(name,roll)
# sos=student()
# sos.one("mahmud",25)
# sos.two("hossain",50)

# class user:
#     def login(self):
#         # self.email=email
#         # self.password=password
#         email=input("enter your email: ")
#         password=input("enter password: ")
#         if email==self.email and password==self.password:
#             login=True
#             print("login successful")
#         else:
#             print("try agian")
# sos=user()
# sos.email="mahmud"
# sos.password="12345"
# sos.login()

# # return a funtion 
# def fun(x,y):
#     sum=x+y
#     return sum

# sos=fun(2,2)
# print(sos)


# def fun(name="mahmud"):
#     print(name)
# fun("hossain")


# pass a lint into a function 
# def fun(phone):
#     for x in phone:
#         print(x)
# sos=("a","b","c")
# fun(sos)


# def fun(s):
#     for x in s:
#         print(x)
# sos=(1,2,3,5,6,7)
# fun(sos)

# def fun():
#     for x in range(1,10):
#         print(x)
# sos=fun()
# sos


# def fun(x,y):
#     if x>y:
#         print("x is getter then y :",x-y)
#     else:
#         print("y is getter then x :",y-x)
# sos=fun
# sos(2,3)
# sos(5,2)
# sos(5,5)


# find odd and even number
# def fun(x):
#     if x%2==0:
#         print("given number is even: ",x)
#     else:
#         print("given number is odd:",x)
# sos=fun
# sos(4)
# sos(5)

# def fun(x):
#     if x%2==0:
#         print("enter number is even:",x)
#     else:
#         print ("enter number is odd",x)

# sos=int(int("enter a intiger number:"))
# fun(sos)



# def fun(x):
#     print(x)
# sos=int(input("enter a int number"))
# fun(sos)
# def fun(name):
#     print("my name is: ",name)
# sos=str(input("enter a name: "))
# fun(sos)

# def fun(sum):
#     print("sum is :",5+sum)
# sos=int(input("enter a number: "))
# fun(sos)


# import math
# print(math.tan(45))

# print(math.acos(0))


# def fun(x,y,z):
#     sum=x+y+z
#     print("result is :",sum)
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number: "))
# fun(a,b,c)

# def fun(*args):
#     print("result is: ",args)
# fun(1,2,3,4,5)


# def fun(*args):
#     for i in args:
#         print(args)
# sos=(1,2,3,4,5)
# fun(sos)

# def fun(*args):
#     totall=0
#     for i in args:
#         totall +=i
#     print(totall)

# sos=fun
# sos(1,2,3,4)
# sos(10,10,10)


# def fn(name,*args):
#     print("my name is: ",name)
#     print("others : ",args)
# fn("mahmud",1,2,3,4)


# def fn(**kwargs):
#     print(kwargs)
# fn(name="mahmud",city="rajshahi")


# def fun(**kwargs):
#     for x, i in kwargs.items():
#         print(f"{x}: {i}")

# fun(name="John", age=30, city="New York")


# def fun(x,y):
#     print(f"my mame is{x} and age is {y}")
# fun("mahmud",26)


# def fun(*args):
#     sum=0
#     for i in args:
#         sum +=i
#     print(f"sum of all args is:",sum)
# fun(1,2,3,4,5)

# def fun(**kwargs):
#     for i,x in kwargs.items():
#         print(f"{i} :{x}")
# fun(name="mahmud",age=25,city="raj")


# def fun(*kwargs):
#     for i in kwargs:
#         print(i)
# fun(1,2,3,4,5)


# def fun19(**kwargs):
#     for args in kwargs:
#         print("{0} : {1}".format(args, kwargs[args]))
# fun19(a=1, b=2, c=3)


# def fun(**kwargs):
#     for i,x in kwargs.items():
#         print(f"{i} : {x}")
# fun(a=1, b=2, c=3)

# def fun():
#     sos=list(range(2,10,50))
#     print(sos)
# fun()

# def fun(name,age,roll):
#     print(f"my name is {name} my is {age} and my roll is {roll} ",sep="!")
# fun("mahmud",28,1)


