# read a txt file

# this code read a specific amount of cherecter
f= open("data/mh.txt","r")
print(f.read(7))

#this code read full txt file with in [] breaket,method 1
with open('mh.txt') as fobj:
    lines =fobj.readlines()
print(lines)

#this code read full txt file with try-except handelling funtion,method 2
try:
    with open('data/mh.txt') as fobj:
        contents=fobj.read()
        print(contents)
except Exception as e:
    print('file not found',e)

# read txt file with enumerate funtion
with open('data/mh.txt') as fobj:
     for x ,y in enumerate(fobj): # here enumerate use for numbering and upper for capital latter
       print(x+1,y.upper())

"""
# read a csv/excel file
import csv
with open('data/excel.csv') as obj:
    fcsv=csv.reader(fobj)

    sum=0
    for i,row in enumerate(fcsv):
        print(i,row[0],row[1])
        sum +=int(row[1]) if i>0 else 0
    print(sum)
"""