# Tuples - tuples are immutable
family = ('Mom','Dad','Brother', 'Sister', "Granny", "Grandpa")

# enumerate() function
# enum = enumerate(family) # return an enumerated object
# print(enum) 
# family_list = list(enum)
# print(family_list) # Return list with tuples

# for index, value in family_list:
#     print(value," at index ",index)

for index, value in enumerate(family):
    print(value," at index ",index)