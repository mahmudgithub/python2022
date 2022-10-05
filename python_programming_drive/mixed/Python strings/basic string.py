# right way
a='Dogs are "love"'
print(a)

# we can call string cherecter induvidually
mh="mahmud hossain"
print(mh[1],mh[2],mh[4])

# we can also call individual string cherecter from last by using -index
mh="mahmud Hossain 12345"
print(mh[1],mh[2],mh[-1],mh[-2])

#right
a="'Dogs' 'are' 'love'"
print(a)

# command string input ,then give output
print("Enter your name:")
x = input()
print("Hello, ", x)

print("Enter your age:")
y = input()
if y<21:
 print("10 age, ")
elif y>22:
 print("yanger")
else:
 print("not maturate")
