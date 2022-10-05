#use re.search funtion ,see output show r is matching and its position 3,4,means: space count,3 pore 4 hosse r er position
import re
mh = "Therin ain Spin"
x = re.search("r", mh)
print(x)

#use re.search funtion ,see output show i is matching and its position 4,5,means: space count,4 pore 5 hosse i er position
import re
mh = "The rin ain Spin"
x = re.search("r", mh)
print(x)

##use re.search funtion ,see output show i is matching and its position count left to right
import re
mh = "The rin ain Spin"
x = re.search("i", mh)
print(x)

##use re.search funtion ,see output show m is not matching and its output non
import re
mh = "The rin ain Spin"
x = re.search("m", mh)
print(x)

##use re.search funtion ,see output show s is matching capital charecter and its position and last position show: so span use to show matching cherecter potion to last position cher
import re
mh= "The rain in Spain"
x = re.search(r"\bS\w+", mh)
print(x.span())

##use re.search funtion ,see output show s is matching capital charecter and its output show total woard: so group use to show total word
import re
mh= "The rain in Spain"
x = re.search(r"\bS\w+", mh)
print(x.group())

