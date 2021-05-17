# Comprehension

"""
    list comprehension
    ------------------
        For-loop
        ----------------
        list = []
        for (iter) in (iterable):
            list.append(output_expression)

        Similar comprehension
        --------------------------------
        [(output_expression) for (iter) in (iterable)]

    Tuple,Set & Dictionary comprehension
    ----------------------------------------------------
    1. Tuple Comprehension : Immutable objects
        ((output_expression) for (iter) in (iterable))

    2. Set Comprehension : Unique and unorderd items
        {(output_expression) for (iter) in (iterable)}

    3. Dictionary Comprehension : key:value pairs
        [(output_expression1) : (output_expression2) for (iter) in (iterable)]
"""

# Example
list = []
for num in range(10):
    list.append(num)
print("for loop output:\t",list)

comp_list = [num for num in range(10)]
print("List comprehension output:\t",comp_list)

# Create a list of square numbers
sqr_list = [num**2 for num in range(10)]
print("Square numbers:\t",sqr_list)

# Tuple comprehension
generator = (num%2 for num in range(10)) # return a generator object
print("tuple comprehension: ",tuple(generator)) # Convert to a tuple

# Set comprehension 
set = {num%2 for num in range(10)}
print("set comprehension: ",set) # consist of only unique values

# Dictionary comprehension
names = ['Amila','Samith','Daniel']
ages = [55,18,36]
dict = {name:age for name,age in zip(names,ages)} 
print("dict comprehension: ",dict)

# if conditions in list comprhension
even_numbers = [num for num in range(10) if num%2==0]
print("even numbers: ",even_numbers)