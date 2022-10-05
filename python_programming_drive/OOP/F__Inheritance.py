#example of multilevel inheritance 
class one:
    def fun1(self):
        print('i am fun1')

class two(one):
    def fun2(self):
        print('i am fun2')


class three(two):
    def fun3(self):
        print('i am fun3')


class four(three):
    def fun4(self):
        print('i am fun4')


lol=four()
lol.fun1()
lol.fun2()
lol.fun3()
lol.fun4()

#use 'super' to call all class method from last inharitence call
class one:
    def fun1(self):
        print('i am fun1')

class two(one):
    def fun2(self):
        print('i am fun2')


class three(two):
    def fun3(self):
        print('i am fun3')


class four(three):
    def fun4(self):
        super().fun1()
        super().fun2()
        super().fun3()
        print('i am fun4')


lol=four()
lol.fun4()

#multiple inheritance example
class one:
    def fun1(self):
        print('i am fun1')

class two:
    def fun2(self):
        print('i am fun2')


class three:
    def fun3(self):
        print('i am fun3')


class four(one,two,three):
    def fun4(self):
        print('i am fun4')


lol=four()
lol.fun1()
lol.fun2()
lol.fun3()
lol.fun4()

#herarachical inheritance but currect 
class one:
    def fun1(self):
        print('i am fun1')

class two(one):
    def fun2(self):
        print('i am fun2')
class three(two):
    def fun3(self):
        print('i am fun3')
lol=two()
#lol=three()
lol.fun1()
lol.fun2()
#lol.fun3()

#herarchic inheritance currect
class one:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def fun1(self):
        print('i am init class')

class two(one):
    def fun1(self):
        print('sum: ', self.x+self.y)

class three(one):
    def fun1(self):
        print('sub: ', self.x-self.y)

lol=two(2,2)
lol.fun1()

lol=three(3,3)
lol.fun1()

#multilevel inheritance
class one:
    def fun1(self):
        print('i am fun1')

class two(one):
    def fun2(self):
        print('i am fun2')
class three(two):
    def fun3(self):
        print('i am fun3')

lol=three()
lol.fun1()
lol.fun2()
lol.fun3()

#multiple inheritance
class one:
    def fun1(self):
        print('i am fun1')

class two(one):
    def fun2(self):
        print('i am fun2')

class three(one):
    def fun3(self):
        print('i am fun3')

class four(two,three):
    def fun4(self):
        print('i am fun4')

lol=four()
lol.fun1()
lol.fun2()
lol.fun3()
lol.fun4()

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


