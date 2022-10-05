#compire given two function then you can easyly understand ,defoult parameter 
def fun1(name,city,roll):
    print('name is',name)
    print('city is',city)
    print('roll is',roll)

fun1('mahmud','rajshahi',123)
#fun1('mahmud','rajshahi')

#on the above program , first object is ok but second not,cause one argument is missing,so show erro. show bellow

#in this function a defoult roll value is given, when second objet willbe call, the defoult value is setup
def fun1(name,city,roll=555):
    print('name is',name)
    print('city is',city)
    print('roll is',roll)

fun1('mahmud','rajshahi',123)
fun1('mahmud','rajshahi')

#this function show error cause ,it not possible to first defoult falue then empty parameter define 
def fun1(name,city='raj',roll):
    print('name is',name)
    print('city is',city)
    print('roll is',roll)

#fun1('mahmud','rajshahi',123)
fun1('mahmud')

#example 
def fun1(name=None, city=None, roll=None):
    print('name is',name)
    print('city is',city)
    print('roll is',roll)

#fun1('mahmud','rajshahi',123)
fun1()

#example
def fun1(name=None, city=None, roll=None):
    print('name is',name)
    print('city is',city)
    print('roll is',roll)

#fun1('mahmud','rajshahi',123)
fun1('mahmud')