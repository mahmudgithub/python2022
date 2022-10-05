#formate1
def fun(self):
    reverse=self[::-1]
    if self==reverse:
        return True
    else:
        return False

print(fun('naman'))
print(fun('mahmud'))

#formate2
def fun(self):
    if self==self[::-1]:
        return True
    return False

print(fun('cool'))
print(fun('oco'))

#by using user input
def fun(self):
    reverse=self[::-1]
    if self==reverse:
        print('treu')
    else:
        print('false')

lol=str(input('enter a string:'))
fun(lol)

#example
def fun(self):
    reverse=self[::-1]
    if self==reverse:
        return True
    else:
        return False

lol=str(input('enter a string:'))
print(fun(lol)) 