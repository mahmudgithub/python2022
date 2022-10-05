x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

x=10
print(x<10 and x>2)

x=10
print(x<9 or x>8)

x=10
print(not(x>9 and x<20))


x=10
if x<12:
    print("true")
else:
    print("fals")