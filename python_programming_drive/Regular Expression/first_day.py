import re

lol=r'[1-9][a-z]'

if re.match(lol,'1we'):
    print('match')
else:
    print('no match')