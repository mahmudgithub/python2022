#Creata new file and write some thing
with open('data/cool.txt','w') as fobj: # here data/cool.txt means creat atxt file in data file ,name is cool
    fobj.write('1234567')                # here 1234567 is crecter that write the file

# add extarnal cherecter to the creating txt file
with open('data/cool.txt','a') as fobj:
     fobj.write("mahmud")
     fobj.write('\n')   #fobj.write('\n') means make new line
     fobj.write('666666666666666')


#write/add bangla cherecter in txt file
with open('data/cool2.txt','w',encoding='UTF-8') as fobj:
    fobj.write('আজকের পোস্ট টি তে দেওয়া ')
    fobj.write('\n')
    fobj.write('আজকের পোস্ট টি ')

# write in file with binary formate
with open('data/cool3.txt','wb') as fobj:
    fobj.write(b'001110')

#chech exist file in harddisk
import os
if os.path.exists('data/cool3.txt'):
    print('yes') # when exist
else:
    print('not')

if os.path.exists('data/cool1.txt'):
    print('yes') #when not exist
else:
    print('not')

"""#write a list in file

list=[['name','age','country'],['mah',24,'us']]
import csv

with open('data/people.csv','w') as fobj:
    fcsv = csv.writer(fobj)
    fcsv.write(list)"""