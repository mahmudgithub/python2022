lol={
    'name':'mahmud',
    'roll':5,
    'city':'raj',
    'old':25
}
print(lol)
print(lol['name'])
print(lol['roll'])
lol['name']='hossain'
print(lol)
if 'roll' in lol:
    print('yes have')
else:
    print('not have')
print(len(lol))
lol['relagion']='islam'
print(lol)
lol.pop('name')
print(lol)
lol.popitem()
print('hi:',lol)
del lol['city']
print('del:',lol)
lol.clear()
print('clear:',lol)
lol.copy()
print(lol)
