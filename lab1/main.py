type(1)    # int
type(-10)  # int
type(0)    # int
type(0.0)  # float
type(2.2)  # float
type(4E2)  # float - 4*10 to the power of 2

# Arithmetic
10 + 3   # 13
10 - 3   # 7
10 * 3   # 30
10 ** 3  # 1000
10 / 3   # 3.3333333333333335
10 // 3  # 3 --> floor division - no decimals and returns an int
10 % 3   # 1 --> modulo operator - return the reminder. Good for deciding if number is even or odd

# Basic Functions
pow(5, 2)       # 25 --> like doing 5**2
abs(-50)        # 50
round(5.46)     # 5
round(5.468, 2) # 5.47 --> round to nth digit
bin(512)        # '0b1000000000' --> binary format
hex(512)        # '0x200' --> hexadecimal format

# Converting Strings to Numbers
age = input("How old are you?")
age = int(age)
pi = input("What is the value of pi?")
pi = float(pi)

type('Hellloooooo') # str

'I\'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab

'Hey you!'[4] # y
name = 'John Doe'
print(name[2])   # h
print(name[:])   # John Doe
print(name[1:])  # ohn Doe
print(name[:1])  # J
print(name[-1])  # e
print(name[::1]) # John Doe
print(name[::-1]) # eoD nhoJ
print(name[0:7:2]) # Jh o
# : is called slicing and has the format [ start : end : step ]

'Hi there ' + 'Timmy' # 'Hi there Timmy' --> This is called string concatenation
print('*'*10) # **********

bool(True)
bool(False)

# all of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

my_list = [1, 2, '3', True] # We assume this list won't mutate for each example below

len(my_list)        # 4
my_list.index('3')  # 2
my_list.count(2)    # 1 --> count how many times 2 appears

my_list[3]          # True
my_list[1:]         # [2, '3', True]
my_list[:1]         # [1]
my_list[-1]         # True
my_list[::1]        # [1, 2, '3', True]
my_list[::-1]       # [True, '3', 2, 1]
my_list[0:3:2]      # [1, '3']

# : is called slicing and has the format [ start : end : step ]

my_list = [1, 2, '3', True] # We assume this list won't mutate for each example below

len(my_list)        # 4
my_list.index('3')  # 2
my_list.count(2)    # 1 --> count how many times 2 appears

my_list[3]          # True
my_list[1:]         # [2, '3', True]
my_list[:1]         # [1]
my_list[-1]         # True
my_list[::1]        # [1, 2, '3', True]
my_list[::-1]       # [True, '3', 2, 1]
my_list[0:3:2]      # [1, '3']

# : is called slicing and has the format [ start : end : step ]

# Add to List
my_list * 2              # [1, 2, '3', True, 1, 2, '3', True]
my_list + [100]          # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
my_list.append(100)      # None --> Mutates original list to [1, 2, '3', True, 100] # Or: <list> += [<el>]
my_list.extend([100, 200]) # None --> Mutates original list to [1, 2, '3', True, 100, 200]
my_list.insert(2, '!!!') # None --> [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.

' '.join(['Hello', 'There']) # 'Hello There' --> Joins elements using string as separator.

# Copy a List
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]

# Remove from List
[1, 2, 3].pop()    # 3 --> mutates original list, default index in the pop method is -1 (the last item)
[1, 2, 3].pop(1)   # 2 --> mutates original list
[1, 2, 3].remove(2)# None --> [1, 3] Removes first occurrence of item or raises ValueError.
[1, 2, 3].clear()  # None --> mutates original list and removes all items: []
del [1, 2, 3][0]   #

# Ordering
[1, 2, 5, 3].sort()                # None --> Mutates list to [1, 2, 3, 5]
[1, 2, 5, 3].sort(reverse=True)    # None --> Mutates list to [5, 3, 2, 1]
[1, 2, 5, 3].reverse()             # None --> Mutates list to [3, 5, 2, 1]
sorted([1, 2, 5, 3])               # [1, 2, 3, 5] --> new list created
list(reversed([1, 2, 5, 3]))       # [3, 5, 2, 1] --> reversed() returns an iterator

# Useful operations
1 in [1, 2, 5, 3]  # True
min([1, 2, 3, 4, 5])# 1
max([1, 2, 3, 4, 5])# 5
sum([1, 2, 3, 4, 5])# 15

# Get First and Last element of a list
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first) # 63
print(last) # 10

# Read line of a file into a list
with open("myfile.txt") as f:
    lines = [line.strip() for line in f]

my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}

my_dict['name'] # John Doe
len(my_dict)    # 3
list(my_dict.keys())   # ['name', 'age', 'magic_power']
list(my_dict.values()) # ['John Doe', 25, False]
list(my_dict.items())  # [('name', 'John Doe'), ('age', 25), ('magic_power', False)]

my_dict['favourite_snack'] = 'Grapes' # {'name': 'John Doe', 'age': 25, 'magic_power': False, 'favourite_snack': 'Grapes'}

my_dict.get('age')      # 25 --> Returns None if key does not exist.
my_dict.get('ages', 0 ) # 0 --> Returns default (2nd param) if key is not found

# Remove key
del my_dict['name']
my_dict.pop('name', None)

my_tuple = ('apple','grapes','mango', 'grapes')
apple, grapes, mango, grapes = my_tuple # Tuple unpacking
len(my_tuple)           # 4
my_tuple[2]             # mango
my_tuple[-1]            # 'grapes'

# Immutability
my_tuple[1] = 'donuts'  # TypeError
my_tuple.append('candy')# AttributeError

# Methods
my_tuple.index('grapes') # 1
my_tuple.count('grapes') # 2

my_set = set()
my_set.add(1)   # {1}
my_set.add(100) # {1, 100}
my_set.add(100) # {1, 100} --> no duplicates!

new_list = [1,2,3,3,3,4,4,5,6,1]
set(new_list)             # {1, 2, 3, 4, 5, 6}

my_set.remove(100)        # {1} --> Raises KeyError if element not found
my_set.discard(100)       # {1} --> Doesn't raise an error if element not found
my_set.clear()            # {}
new_set = {1,2,3}.copy()  # {1, 2, 3}

set1 = {1,2,3}
set2 = {3,4,5}

set3 = set1.union(set2)                # {1,2,3,4,5}
set4 = set1.intersection(set2)         # {3}
set5 = set1.difference(set2)           # {1, 2}
set6 = set1.symmetric_difference(set2) # {1, 2, 4, 5}
set1.issubset(set2)                    # False
set1.issuperset(set2)                  # False
set1.isdisjoint(set2)                  # False --> return True if two sets have a null intersection.

type(None) # NoneType
a = None