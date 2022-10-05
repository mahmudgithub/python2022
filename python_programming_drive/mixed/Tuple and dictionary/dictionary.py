
mh={} # dictionary 3rd/karli braket diya lika hoy
mh['name']='mahmud' # we can difine string type
mh[555]=111         # we can difine int type
print(mh['name'],'|', mh[555])

# we can ddefine funtion in dictionary
mh={'m':'01738750','h':'015214720'}
print(mh['m'],'|',mh['h'])

# add item in dictionary
mh={'rice':40,'oil':30,'egg':8} # first added items
print(mh)
mh['fish']=80 # after add itms
mh['watermellon']=20
print(mh)

# delet item from dictionary
mh={'rice':40,'oil':30,'egg':8} # first added items
print(mh)
mh['fish']=80 # after add itms
mh['watermellon']=20
del mh['oil']
print(mh)

# use items funtion
mh={'a':20,'b':30,'c':40,'d':50,'e':60}
for x,y in mh.items():
    print(x,y,sep='=') # here x is item name,y is value

#use key funtion for name
mh={'a':20,'b':30,'c':40,'d':50,'e':60}
for x in mh.keys():
    print(x)

#use values funtion for valu
mh={'a':20,'b':30,'c':40,'d':50,'e':60}
for x in mh.values():
    print(x)

# use sorted in dictionary
mh={'rich':50,'egg':12,'water':10,'apple':30}
print(mh)
for x in sorted(mh.keys()):
    print(x,mh[x])



