#overriding by construct method
class one:
    def __init__(self):
        print('i am first')

class two(one):
    def __init__(self):
        super().__init__()
        print('i am second')
lol=two()

# overriding access by super
class one:
    def fun(self):
        print('i am first')

class two(one):
    def fun(self):
        super().__init__()
        print('i am second')

lol=two()
lol.fun()


#overriding by instance method
class one:
    def fun(self):
        print('i am first')

class two(one):
    def fun(self):
        print('i am second')

lol=two()
lol.fun()

#apply super in overrinding instance method
class one:
    def fun(self):
        print('i am first')

class two(one):
    def fun(self):
        super().fun()
        print('i am second')

lol=two()
lol.fun()

#simple anoter init making overriding example
class one:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('sum:',x+y)

class two(one):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('mutipication:',x*y)

lol=two(2,2)

#using parent and child method if the method is overriding  or not using super (instance method )
class one:
    def fun(self,x,y):
        self.x=x
        self.y=y
        print('sum:',x+y)

class two(one):
    def fun(self,x,y):
        self.x=x
        self.y=y
        print('mutipication:',x*y)

lol=two()
lol.fun(2,2)

sos=one()
sos.fun(2,2)

#using parent and child method if the method is overriding  or not using super (__init__ method)
class one:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('sum:',x+y)

class two(one):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('mutipication:',x*y)

lol=two(2,2)
sos=one(2,2)

#overloading ,in python method over loading is not possible but try to an dame example ,which is not work
class one:
    def fun(self):
        print('sum')

    def fun(self,x):
        self.x=x

        print('mutipication:',x)

sos=one()
sos.fun()
sos.fun(2)

#example 2, by init method 
class one:
    def __init__(self):
        print('hello')

    def __init__(self,x,y):
        self.x=x
        self.y=y
        print('mutipication:',x*y)
sos.one()
sos=one(2,2)
#use super alter formula in method overriding 
class one:
    def __init__(self):
        print('i am init method 1')

    def fun(self):
        print('i am fun1')

class two:
    def __init__(self):
        print('i am init metod 2')

    def fun(self):
        print('i am fun2')

class three(one,two):
    def __init__(self):
        one.__init__(self)
        two.__init__(self)
        print('i am init method 3')

    def fun(self):
        one.fun(self)
        two.fun(self)
        print('i am fun3')

lol=three()
lol.fun()