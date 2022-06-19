def countdown(num):
    array = []
    for x in range(num,-1, -1):
        array.append(x)
    return(array)

print(countdown(10))


def print_and_return(num1,num2):
    print(num1)
    return(num2)

print_and_return(5,3)


array = [1,2,3,4,5]

def add_it_up(list):
    sum = array[0] + len(array)
    return(sum)

sum = add_it_up(array)
print(sum)

list = [5,2,3,2,1,4]
def values_greater_than_second(list):
    list_2 = []
    if len(list) < 2:
        return("False")

    for x in list:
        if x >= list[2]:
            list_2.append(x)
    print(f"The length of the list is {len(list_2)} and the values of the list are {list_2}.")
values_greater_than_second(list)


def length_and_value(num1,num2):
    array = []
    for x in range(num1):
        x = [num2]
        array.append(x)
    return(array)

result = length_and_value(3,1)
print(result)



