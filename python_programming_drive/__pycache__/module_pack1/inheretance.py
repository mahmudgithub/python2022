class one:
    def fun1(self,id,gpa):
        self.id=id 
        self.gpa=gpa

    def fun2(self,color):
        self.colo=color

class two(one):
    def fun3(self):
        print("id:",self.id,"gpa:",self.gpa,"color:",self.color)
        