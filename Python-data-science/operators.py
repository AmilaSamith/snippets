# Arithmetic Operators

"""
    Order of precedence
    --------------------------------------------------------
    ()  : paranthesis 
    **  : Exponent
    *   : Multiplication
    /   : Division
    +   : Addition
    -   : Subtraction 
"""

print(5+10) # Addition
print(5-10) # Subtraction
print(5/10) # Division
print(5//2) # Floor division : No of times 2 go evenly into 5
print(5*10) # Multiplication
print(52%10)# Modulus : Remainder after division
print(2**3) # Exponent

# Comparison Operators

"""
    ==  : equals                    
    ! = : not equal                 
    >   : greater than
    <   : less than
    > = : greater than or equal
    < = : less than or equal
"""

# Logical operators - Use to combine conditional statements.

"""
    and : 	Returns True if both statements are true	                    x < 5 and  x < 10	
    or  :	Returns True if one of the statements is true	                x < 5 or x < 4	
    not :	Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)
"""

# Membership operators

"""
    in      : 	Returns True if a sequence with the specified value is present in the object	    x in y	
    not in  :	Returns True if a sequence with the specified value is not present in the object	x not in y

"""

# Example for membership operators
x = ["apple", "banana"]
print("banana" in x) # return True
print("orange" not in x) # return True

# Identity operators
"""
    is      :	Returns True if both variables are the same object	        x is y	
    is not  :	Returns True if both variables are not the same object	    x is not y
"""

# Example for identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
# difference betweeen "is" and "=="
print(x == y) # returns True because x is equal to y
