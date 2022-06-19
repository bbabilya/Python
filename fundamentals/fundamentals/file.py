num1 = 42
num2 = 2.3
# variable declaration + numbers
boolean = True
#boolean
string = 'Hello World'
#string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#string array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#object array
fruit = ('blueberry', 'strawberry', 'banana')
#string array
print(type(fruit))
#log statement
print(pizza_toppings[1])
#log statement
pizza_toppings.append('Mushrooms')
#add value
print(person['name'])
#log statement 'name' in object array person
person['name'] = 'George'
#change value
person['eye_color'] = 'blue'
#change value
print(fruit[2])
#log statement fruit index 2

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
    #if and else statement + log statement
    #will print else statement "It's lower"

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#if/elseif/else statement for string length, will print "Just right!"

for x in range(5):
    print(x)
#for loop that goes up to 5
for x in range(2,5):
    print(x)
#for loop that starts at 2 and ends at 5?
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)
#delete value

print(person)
#log statement
person.pop('eye_color')
#delete value 'eye_color'
print(person)
#log statement w/o eye_color

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
#function
    for num in range(10):
#parameter
        print('Hello')
#log statement


print_hello_ten_times()
#call function

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
"""
Hello
Hello
Hello
Hello
"""

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
"""
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
"""

print_hello_x_or_ten_times()
#function call defined as x = 10 on above function
print_hello_x_or_ten_times(4)
#function call that will return: 
"""
Hello
Hello
Hello
Hello
"""


"""
Bonus section
"""

# print(num3)
#log statement "72"
# num3 = 72
#variable declaration
# fruit[0] = 'cranberry'
#change value at fruit index 0 to cranberry
# print(person['favorite_team'])
#KeyError
# print(pizza_toppings[7])
#IndexError
#   print(boolean)
#log statement "true"
# fruit.append('raspberry')
#add value
# fruit.pop(1)
#delete value