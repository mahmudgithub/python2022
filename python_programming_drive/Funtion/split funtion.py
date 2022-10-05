import re
mh = "The all mighty ALLAH"
x = re.split("\s", mh)
print(x)

import re
mh="The all mighty     ALLAH i love u very much"
x=re.split("\s",mh,3)
print(x)