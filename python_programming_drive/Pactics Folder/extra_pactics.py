from operator import is_not

print("mahmud",end="_")
print("hossain")

#print('\a\bsss\fss\nd\tmi')
#print('\a') # for create bip sound
print('mahmud \bhossain') # back-space
print('\f') #
print('mahmud_\nhossain') #line break
print('mahmud\thossain') # tab
print('mahmud\vhossain') #virtical tab
#input('type a name:')
print('hello'+'mahmud')
print('hello_world'*2)
print('5'*2)
print(2*'5')
print(2*'mahmud')
mahmud = "My self score on PHP: {0}, Python: {1}, Java: {2}, Swift: {3}". format(6, 6.5, 5, 6)
print(mahmud)

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('{0}{1}{0}'.format('abra', 'cad'))

message = "If x = {x} and y = {y}, then x+y = {z}".format(x = 20, y = 300, z = 20+300)
print(message)

num1=2
num2=2
print(f"{num1}+{num2} = {num1+num2}")

print("frut, ".join(["apple", "orange", "pineapple","cool"]))
#print("mahmud").replace("apple")

print("This is a my sentence.".startswith("This"))
print("This is a sentence.".startswith("is"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".endswith("my"))

print("this is a sentence.".upper()) 
print("This is A sentence.".upper())

print("AN ALL CAPS SENTENCE".lower())
print("AN all CAPS SENTENCE".lower())

print("m,a,h,m,u,d".split(", "))

print (int("123"))
print (int(12.3))
print (str(123))
print (str(12.3))
print (int("123"))
print (float(12.3))

x = 7
print(x)
print(x + 3)

x = 7.5
print(x)
x="hello"
print(x + "3")

#user_input = input("Enter your birth year: ")
#age = 2020 - float(user_input) #here float,int etc use
#print("You are " + str(age) + " years old!")

a = 3
a += 2
print(a)

language = "Python"
language += "3"
print(language)

if 2>1:
    print("2 is greater then 1")

mahmud=15
if mahmud>10:
    print("mahmud is bigger")
    if mahmud<10:
        print("mahmud is small")

if 20>30:
    print("20 is less then 30")
else:
    print("20 is geter then 30")

num=20
if num>15:
    print("num is geter then 15")
else:
    if num>18:
        print("num also geter then 18")
    else:
        if num>22:
            print("num is less then 22")
        else:
            print("condition 4 is true")


love=100
if love<99:
    print("what is love")
elif love>100:
    print("great love")
else:
    print("i did not like love")



a = 100
b = 200 
if (a >= 100 and a < 200): 
    print(b)
else: 
    print(300)

a = 100
b = 200 if (a >= 100 and a < 200) else 300
print(b)


status  = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

for mah in range(10):
    print(mah)
else:
    print("not")

a= 1 is 1 and 2 is 2
print(a)

a= 1 is not 1 and 2 is 2
print(a)

i=10
while i<100:
    print(i)
    i=i+1

m=5
while m<2:
    print(m)
    m=m+1

i=10
while i<100:
    print(i)
    i=i+1
    if i==50:
        print("ok start again")
        continue

i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

print("Finished")

def my(x,y):
    sum=x+y
    print(sum)
my(2,3)

def coll():
    print("hello world")
coll()

def lol(x=2,y=3):
    sum=x+y
    print(sum)
lol()

def double(x):
    sum=x*2
    print(sum)
double(2)
double(5)

def multi_sum(x,y):
    mul=x+y
    print(mul)
multi_sum(2,2)
multi_sum(3,3)

def new(*args):
    print(args)
new(2,3,4,5,6)

for my in range(10):
    my=my+1
    print(my)

name=["mah","do","did","done"]
print(name[0])
print(name[2])

str = "Hello world!"
print(str[6])


replace_num = [1, 2, 3, 5]
replace_num[3] = 100
print(replace_num)

append_list = [1, 2, 3]
print(append_list + [100, 200, 300])

print(append_list * 3)

food=[1,2,3,4,5,6,7]
print(food[5])

food=["apple","banana","coco"]
print(food[2])
print("coco" in food)

food=["apple","banana"]
food[1]="jam"
print(food)

print("coco" in food)
print("coco" not in food)

def cool(x,y,z):
    sum=x+y-z
    print(sum)
cool(2,2,2)

def coco(*args):
    print(args)
coco(1,2,3,4,5,6)
#coco(a=2,b=3,c=4)

def colo(**kwargs):
    print(kwargs)
colo(a=2,b=3,c=4)

def mah(*args):
    for x in args:
        print(x)
mah(1,1,1,1,1,)

def mah(*args):
    for x in args:
        print(x)
mah(1,1,1,1)

def print_dict(**kwargs):
    for ma in kwargs:
        print(ma)

print_dict(a=1, b=2, c=3,d=4)


x=10
def new(y):
    if x>y:
        print("x is big then y")
        print(x)
    else:
        print("y is big then x")
        print(y)

new(5)
new(15)

x=5
def new(y):
    if x>y:
        print("x is big then y:",end="")
        print(x)
    else:
        print("y is big then x:",end="")
        print(y)
new(3)
new(9)


def parameter (x, y):
    if x > y:
        return x
    else:
        return "hello"
argument = parameter(23, 32)
print(argument)

def cool(x,y):
    return "wow"
hi=cool(2,3)
print(hi)


def add_numbers(x, y):
    total = x + y
    print("This won't be printed")
    return total
print(add_numbers(4, 5))

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))

def name(xy):
    print("my name is " + xy + " hossain");
name("mahmud");

def Greet(name):
    print("Hello, " + name + ". Good morning!");
     
Greet("Masud");

def getSum(num1, num2):
    sum = num1 + num2;
    print("Sum of the two numbers ",num1," and ",num2,"  is : ", sum);
getSum(num2=30, num1=20);


def greet(*args):
   for name in args:
       print("Hello",args)
greet("Monir","Minhaz","Iqbal","Sharif")
greet(1,2,3,4)

def greet(*kwargs):
   for name in kwargs:
       print("Hello",kwargs)
greet("Monir","Minhaz","Iqbal","Sharif")
greet(1,2,3,4)


def greet(**kwargs):
   for name in kwargs:
       print("Hello",kwargs)
greet(a="Monir",b="Minhaz",c="Iqbal",d="Sharif")
greet(a=1,b=2,c=3,d=4)

def add_explanation(line):
    return line + '!'
update_line = add_explanation
print(update_line("Hello World"))

def vim(sos):
    return 1+sos
update=vim
print(update(22))

def dod(x,y):
    if x>y:
        print("hello world")
    else:
        print("nothing")
dod(2,3)
 
def did(a,b):
   print("hello mann")
   z=a+b
   return a

did(1,3)


def mom(**kwargs):

    print(kwargs)
    return "lamyaa"
mom(x=2,y=3)

class mama():
    def ma1(x,y):
        sum=x+y
        print(sum)
    ma1(x=2,y=3)

    def ma2(w,z):
        sub=w-z
        print(sub)
    ma2(z=4,w=5)

import math
print (math.tan(45))


def dod(x,y=0):
    sum=x
    print(x)
    print(y)
    return x+y,x,y
print(dod(2,4))



def name(nam):
    print("my name is " +nam)
your_name=input("give your name:")
name(your_name)

def number(odd):
    if odd%2==0:
        print("it is even number")
    else:
        print("it is odd number")
        return number
given=int(input("enter any number:"))
number(given)



class Hello:
    def me1():
        print ("Hello one")
    def me2():
        print ("Hello two!")
    def me3():
        print ("Hello three")

Hello.me1()
Hello.me2()
Hello.me3()


class world:
    def bangladesh(self):
        print("i am bangladesh")
    def india(self):
        print("i am india")
    def packistan(self):
        print("i am pakistan")
out1=world()
out1.bangladesh()

out2=world()
out2.india()

out3=world()
out3.packistan()

from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World!')
    print (HttpResponse('hello'))

#print(index()) 

letters = ['a', 'b', 'c', 'd', 'e']
for i in letters:
    #pass
    print(i)

x = 256
x is 256
## ey funtion teke j kono integer er ASCII code powa jabe
def f1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string

int_list = [1,97, 98, 99,110]
print(f1(int_list))

