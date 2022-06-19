x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#change the value of 10 to 15, no need for function
x[1][0] = 15

#create a function that given a list of dictionaries, the function loops through each dictionary and prints each key and value.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for x in list:
        print(f"{'first_name'} = {x['first_name']}, {'last_name'} = {x['last_name']}")

iterateDictionary(students)

#given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 
def iterateDictionary2(key_name, list):
    for x in list:
        print(x[key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for x in dict:
        print(len(dict[x]), x)
        for y in dict[x]:
            print(y)

printInfo(dojo)
