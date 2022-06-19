# #basic
for x in range(150+1):
    print(x)

# #multiples of five
for x in range(5,1000+1):
    if x % 5 == 0:
        print(x)

# #Counting the Dojo Way
for x in range(1,100+1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#Whoa, that sucker's huge!
sum = 0
for x in range(1,500000):
    if x % 2 != 0:
        sum = (sum + x)
print(sum)

#Countdown by Fours
for x in range(2018,0,-4):
    print(x)

#Flexible Counter
lowNum = 2
highNum = 200
mult = 4
for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)