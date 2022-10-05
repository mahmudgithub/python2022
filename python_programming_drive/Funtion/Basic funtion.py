def mh(): # here def constant,mh variable name
  print("Hello from a function")
mh() # call a empty funtion


def mh(name):
    print("Hello, " + name + ". Good morning!")
mh('Mahmud') # call a name type  funtion
mh('Hossain')


def mh(name,msg): # call a name & msg two  funtion
   print("Hello",name + ', ' + msg)
mh("Monica","Good morning!")


def mh(value): # use a return value in a funtion
 if value >0:
  return value
 else:
  return -value
print(mh(2))
print(mh(-4))

def name(mh):
    print("name {mh}".format(mh=mh))
    print("Welcome {mh}".format(mh=mh))
name('mahmud')
name('hossain')

#potional agrument
def person (name,age,country):
    print(name,age,country, sep='|')
person('mh','12','uk')

#keyword argument
def person(name,age,country):
    print(name,age,country,sep='|')
person(name='Mh',age=24,country='bang')

#use keyward and positional argument

def person(name,age,country='Bangladesh'): # here Bangladesh by defolt country
    print(name,age,country,sep='|')
person(name='mahmud',age=25,country='uk')
person(name='mahmud',age=24)  # use key ward argument with by default country
person('mahmud',24) # use position argument with by default country

# return value funtion
def mh(x,y):

   # return 2
#print(mh)
mh(2,3)