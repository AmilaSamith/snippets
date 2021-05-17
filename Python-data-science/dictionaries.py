# Dictionary - A dictionary contains key-value pairs.

dict = {"Name":"Amila", "Age":25, "University":"RUH"}

# Get all keys in dictionary.
keys = dict.keys()
print(keys)

# Get list of values in dictionary.
values = list(dict.values())
print(values)

int_list = [10, 11, 20, 56]
soe = sum(int_list) # Get sum of elements
print(soe)

ages = {"sam":55,"Brian":23,"John":35,"Smith":18}
"""looping through a dictionary"""
# Method 01
for key in ages:
    print(key,"",ages[key])

# Method 02
for key, value in ages.items(): # ages.items() : return a list of tuples 
    print(key,"",value)