class one:
    def fun1(self,name,roll):
        self.name=name
        self.roll=roll 
        print("name:",self.name, "roll:",self.roll)

    def fun2(self,name,roll,city):
        self.city=city 
        self.name=name
        self.roll=roll 
        print("name:",self.name, "roll:",self.roll,"city:",self.city)


hi=one()
hi.fun1("mahmud",123)
hi.fun2("mahmud",123,"raj")