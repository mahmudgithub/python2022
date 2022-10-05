#any character except for a new line
import re

text = 'machinelearningplus.com'
print(re.findall('.', text))  # .   Any character except for a new line
print(re.findall('...', text))

#period
text = 'machinelearningplus.com'
print(re.findall('\.', text))  # matches a period
print(re.findall('[^\.]', text))  # matches anything but a period

#Any digit
text = '01, Jan 2015'
print(re.findall('\d+', text))  # \d  Any digit. The + mandates at least 1 digit.

#Anything but a digit
text = '01, Jan 2015'
print(re.findall('\D+', text))  # \D  Anything but a digit

#Any character, including digits
text = '01, Jan 2015'
print(re.findall('\w+', text))  # \w  Any character

#Anything but a character
text = '01, Jan 2015'
print(re.findall('\W+', text))  # \W  Anything but a character

#Collection of characters
text = '01, Jan 2015'
print(re.findall('[a-zA-Z]+', text))  # [] Matches any character inside

#Match something upto ‘n’ times
text = '01, Jan 2015'
print(re.findall('\d{4}', text))  # {n} Matches repeat n times.
print(re.findall('\d{2,4}', text))

#Match 1 or more occurrences
print(re.findall(r'Co+l', 'So Cooool'))  # Match for 1 or more occurrences

#Match any number of occurrences (0 or more times)
print(re.findall(r'Pi*lani', 'Pilani'))

import re

pattern = r"Bangladeshi"

result = re.match(pattern, "Bangladesh")

if result:
    print("Match Found!")
else:
    print("No match")


import re

pattern = r"Bangladesh"

if re.search(pattern, "There is country named Bangladesh in south asia!"):
    print("Match Found!")
else:
    print("No match")

pattern = r"bangla"    
print(re.findall(pattern, "Bangladeshi bangla and indian bangla are differnet."))

import re

pattern = r"bin"

match = re.search(pattern, "combination")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")

import re

pattern = r"^wr.te$"

if re.match(pattern, "write"):
   print("Match 1")

if re.match(pattern, "wrote"):
   print("Match 2")   

if re.match(pattern, "writer"):
   print("Match 3")


import re

# A character set containing all vowels
pattern = r"[aeiou]"

# Lets check whether a word got a vowel in it or not
if re.search(pattern, "grey"):
   print("The word 'grey' got at least one vowel!")


import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "NS1 is prefix of first name server address."):
   # Found NS1 as match
   print("OK")

if re.search(pattern, "You should put a second one with NS2 as prefix."):
   # Found NS2 as match
   print("OK")

if re.search(pattern, "I don\'t have any nameserver."):
   print("NS3")
else:
   print("Not OK!")

if re.search(pattern, "PY3K"):
   # Found PY3 as match
   print("OK")
else:
   print("No vowel found!")

if re.search(pattern, "qwertyuiop"):
   print("The word 'qwertyuiop' got at least one vowel!")
else:
   print("No vowel found!")

if re.search(pattern, "rhythm myths"):
   print("The word 'rhythm myths' got at least one vowel!")
else:
   print("No vowel found!")


import re

# Match string that contains NOT ALL Capital letters
pattern = r"[^A-Z]"

if re.search(pattern, "a sentence with all lower case letters."):
   print("Match 1")

if re.search(pattern, "A sentence with mixed English letters."):
   print("Match 2")

if re.search(pattern, "HEADING"):
   # All Capital letters
   # No Match
   print("Match 3")

if re.search(pattern, "HEADING WITH ALL CAPITAL LETTERS"):
   # All Capital letters 
   # but "spaces" makes it True to NOT ALL Capital
   print("Match 4")


import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())


import re


blog_path_1 = '/blog/1/'
blog_path_2 = '/blog/2/'
blog_path_3 = '/blog/34/'
blog_path_4 = '/blog/winter-is-coming/'

matching_digits_regex = r'^/blog/(?P<id>\d+)/$'
        
def get_id(path):
    p = re.compile(matching_digits_regex)
    print('{}\'s id is {}'.format(path, p.search(path).group('id')))

get_id(blog_path_1)
get_id(blog_path_2)
get_id(blog_path_3)

try:
    get_id(blog_path_4)
except:
    print("{} does not have a matching id".format(blog_path_4))

print("\n")

matching_slug_regex = r'^/blog/(?P<slug>[\w-]+)/$'
def get_slug(path):
    p = re.compile(matching_slug_regex)
    print('{}\'s slug is {}'.format(path, p.search(path).group('slug')))

get_slug(blog_path_1)
get_slug(blog_path_2)
get_slug(blog_path_3)
get_slug(blog_path_4)

text = 'machinelearningplus.com'
print(re.findall('\.', text))  # matches a period
print(re.findall('[^\.]', text))  # matches anything but a period
# use of ['.']

text = '01, Jan 2015'
print(re.findall('\d+', text))  # \d  Any digit. The + mandates at least 1 digit.
#> ['01', '2015']

text = '01, Jan 2015'
print(re.findall('\D+', text))  # \D  Anything but a digit
#> [', Jan ']

text = '01, Jan 2015'
print(re.findall('\w+', text))  # \w  Any character

text = '01, Jan 2015'
print(re.findall('[a-zA-Z]+', text))  # [] Matches any character inside
#> ['Jan']

text = '01, Jan 2015'
print(re.findall('\d{4}', text))  # {n} Matches repeat n times.
print(re.findall('\d{2,4}', text))
#> ['2015']
#> ['01', '2015']

print(re.findall(r'Co+l', 'So Cooool'))  # Match for 1 or more occurrences
#> ['Cooool']

print(re.findall(r'Pi*lani', 'Pilani'))
#> ['Pilani']

