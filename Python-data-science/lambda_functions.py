# Lambda fuctions

"""
    lambda syntax
    ----------------------------------------------------------------
    lambda (inputs) : (output_expression)
"""

# Example 01
add = lambda x,y: x + y
print(add(4,6))
print((lambda x,y: x + y)(4,10))

# Example 02
ages = {"michel":50,"martha":45,"vince":18,"Hilton":23}

def getVal(item):
    return item[1]

sortedList = sorted(ages.items(), key=getVal)

print(ages)
print(sortedList)

# Similar Lambda function

lambdaSorted = sorted(ages.items(), key= lambda item: item[1])

print(lambdaSorted)

# Example 03 : Filter data from a list

nums = [11,12,45,78,147,56,89,22,48,102]
# Get list of odd numbers
odds = filter(lambda num: num%2 == 1,nums)
print(list(odds))

# Example 04 : Perform an operation to each elemnt in a list
nums = [x for x in range(20)]
sqr = map(lambda x:x**2,nums)
print(list(sqr))