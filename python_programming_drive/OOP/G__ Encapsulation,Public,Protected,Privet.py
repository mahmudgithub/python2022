#example:1 (right formula, cause public,protected,privet check korar jonne function er bire teke call korte hobe)
# how khown public,protected,privet access by using instance method 
class one:
    def __init__(self,name):
        self.name=name
        self._name=name
        self.__name=name
    def fun1(self):
        pass
        #print('public:',self.name)

    def fun2(self):
        pass
        #print('protected:', self._name)

    def fun3(self):
        pass
        #print('privet:',self.__name)

lol=one('mahmud')
lol.fun1()
lol.fun2()
lol.fun3()
print('public:',lol.name)
print('protedted:',lol._name)
print('privet:',lol.__name)

#example:2 (wrong formula, cause ,call kora hoyse function er vetor teke)
class one:
    def __init__(self,name):
        self.name=name
        self._name=name
        self.__name=name
    def fun1(self):
        print('public:',self.name)

    def fun2(self):
        print('protected:', self._name)

    def fun3(self):
        print('privet:',self.__name)


lol=one('mahmud')
lol.fun1()
lol.fun2()
lol.fun3()

#example:3(right formula)
# how khown public,protected,privet access by using only init method 

    def __init__(self,name):
        self.name=name
        self._name=name
        self.__name=name
lol=one('mahmud')
print('public:', lol.name)
print('protected:', lol._name)
print('privet:', lol.__name)

