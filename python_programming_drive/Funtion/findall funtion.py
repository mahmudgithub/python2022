import re
mahmud="i love my country lo"
x=re.findall("lo",mahmud)
print(x)

import re
hossain="mahmud mahmud mahmud"
x=re.findall("mahmud",hossain)
print(x)

import re
m="123456789"
x=re.findall("1359",m)
print(x)

#use re.findall[a-m]: means a to m er moddekar cherecter gulo sudo show korbe
import re
mh="he is my god so i love him"
x=re.findall("[a-m]",mh)
print(x)

# use re.findall("\d") find all digit characters:
import re
mh = "That will be 59 dollars"
x = re.findall("\d", mh)
print(x)

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
import re
mh = "hello world"
x = re.findall("he..o", mh) #first 2 charecter,pore joto ta cherecter add hobe toto ta ... add ,j porjonto cherecter nibo sey cherecter
print(x)

#use re.findall("^hello") Check if the string starts with 'hello' or not:
import re
mh = "hello world"
x = re.findall("^g", mh)
if (x):
 print("Yes, the string starts with 'hello'")
else:
 print("no")

# use re.findall("world$") Check if the string ends with 'world or not':
import re
mh = "hello world"
x = re.findall("world$", mh)
if (x):
     print("Yes, the string ends with 'world'")
else:
     print("No")


# use re.findall("falls|stays") Check if the string contains either "falls" or "stays":
import re
mh = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", mh)
print(x)
if (x):
 print("Yes, there is at least one match!")
else:
 print("No match")


#use re.findall("n{5}" Check if the string contains "n" followed by exactly two "l" characters: means por por 5 ta n ase ki?
import re
mh = "The rainnnnn in Spain falls mainly in the plain!"
x = re.findall("n{5}", mh)
print(x)
if (x):
 print("Yes, there is at least one match!")
else:
 print("No match")


#Check if the string contains "ai" followed by 1 or more "x" characters:
import re
mh = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix+", mh)
print(x)
if (x):
 print("Yes, there is at least one match!")
else:
 print("No match")

#Check if the string contains "ai" followed by 0 or more "x" characters:
import re
mh = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*", mh)
if (x):
 print("Yes, there is at least one match!")
else:
 print("No match")