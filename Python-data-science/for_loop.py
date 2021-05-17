# For-loop condition

"""
    for-loop
    --------------------------------
    for (iter) in (iterable):
        (code to be executed while have iter in iterable)
"""

for num in [1,2,3,4]:
    print(num)

# range() function
"""
    range(start*,stop,step*) - * optional params
"""

for num in range(2,10,2):
    print(num)

# Loop control statements

""" break keyword """
for num in range(10):
    if num == 5:
        break # break the loop when if condition is satisfied
    print(num)

""" continue keyword """
for num in range(10):
    if num == 5:
        continue # continue to next iteration skipping the code below.
    print(num)

""" 
    pass keyword 
    ----------------------------------------------------------------
    This is used as a placeholder when running the code.
    Used as a placeholder for future code.
    When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
    Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

    Examples
    --------

    def myfunction():
        pass

    for x in [0, 1, 2]:
        pass
"""