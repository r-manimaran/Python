# Advanced Unpacking
# - Unpacking refers to splitting up an interval object and grabbing its individual elements.

# 1. Basic Unpacking
a,b,c = [1,2,3]
print(f'a:{a},b:{b},c:{c}\n')
# Output:a:1,b:2,c:3

# Extended Iterable Unpacking with *
a,b,*c = [1,2,3,4,5]
print(f'a:{a}, b:{b}, c:{c}\n')
# Output:a:1,b:2,c:[3,4,5]

*a,b,c = [1,2,3,4,5]
print(f'a:{a}, b:{b}, c:{c}\n')
# Output:a:[1,2,3],b:4,c:5

a,b,*c,d = [1,2,3,4,5,6,7]
print(f'a:{a}, b:{b}, c:{c}, d:{d}\n')
# output:a:1, b:2, c:[3,4,5,6], d:7

# Unpacking with nested lists
a,b,[c,d] = [1,2,[3,4]]
print(f'a:{a}, b:{b}, c:{c}, d:{d}\n')
# Output:a:1, b:2, c:3, d:4

a,b,[*c,d] = [1,2,[3,4,5,6]]
print(f'a:{a}, b:{b}, c:{c}, d:{d}\n')
# Output:a:1, b:2, c:[3,4,5], d:6

# Unpacking with nested tuples
a,b,(c,d) = [1,2,(3,4)]
print(f'a:{a}, b:{b}, c:{c}, d:{d}\n')
# Output:a:1, b:2, c:3, d:4 

# Unpacking with nested tuples and *
a,b,(c, *d) = [1,2,(3, 4, 5)]
print(f'a:{a}, b:{b}, c:{c}, d:{d}\n')
# Output:a:1, b:2, c:3, d:[4, 5]

#Ignoring values with _
# _ means anonymus variable
a,b, _ = [1,2,3]
print(f'a:{a}, b:{b}\n')
# Output:a:1, b:2

a,b, *_ = [1,2,3, 4,5]
print(f'a:{a}, b:{b}\n')
# Output:a:1, b:2

*a,b, _ = [1,2,3, 4,5]
print(f'a:{a}, b:{b}\n')
# Output:a:[1,2,3],b:4

a,b, *_ ,d = [1,2,3, 4,5,6,7]
print(f'a:{a}, b:{b}, d:{d}\n')
# Output:a:1, b:2, d:7

#Unpack Nested structures
data = ("Alice",(22,"Engineer"))
name, (age, profession) = data
print(f'Name: {name}, Age: {age}, Profession: {profession}\n')
# Output:Name: Alice, Age: 22, Profession: Engineer

# Unpacking with for loop
data = [(1,2), (3,4), (5,6)]
for a, b in data:
    print(f'a:{a}, b:{b}')
    # Output:a:1, b:2
    # Output:a:3, b:4
    # Output:a:5, b:6

# Unpacking with for loop and *
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, *c in data:
    print(f'a:{a}, b:{b}, c:{c}')
    # Output:a:1, b:2, c:[3]
    # Output:a:4, b:5, c:[6]
    # Output:a:7, b:8, c:[9]

# Unpacking with for loop and _
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, _ in data:
    print(f'a:{a}, b:{b}')
    # Output:a:1, b:2
    # Output:a:4, b:5
    # Output:a:7, b:8

# Unpacking in Function arguments
def print_names(*names):
    for name in names:
        print(name)

# call print_names with a list of names
names = ["Alice", "Bob", "Charlie"]
print_names(*names)
# Output:Alice
# Output:Bob
# Output:Charlie

#combining lists and unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print(f"combined List:{combined_list}\n")
#output: combined List:[1, 2, 3, 4, 5, 6]

#combining dictionaries and unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined_dict = {**dict1, **dict2}
print(f"combined Dict:{combined_dict}\n")
#output: combined Dict:{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#combining lists and dictionaries and unpacking
list1 = [1, 2]
dict1 = {'a': 3, 'b': 4}
combined_data = [*list1, *dict1.items()]
print(f"combined Data:{combined_data}\n")
#output: combined Data:[1, 2, ('a', 3), ('b', 4)]

#swapping variables using unpacking
a = 1
b = 2
print(f"Before swap: a={a}, b={b}")
a,b = b,a
print(f"After swap: a={a}, b={b}\n")
#output:Before swap: a=1, b=2
#output:After swap: a=2, b=1

#returning multiple values from a function
def get_name_and_age():
    return "Alice", 30

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}\n")
#output:Name: Alice, Age: 30

#returning multiple values from a function and unpacking
def get_person_details():
    return "John", 25, "Engineer"