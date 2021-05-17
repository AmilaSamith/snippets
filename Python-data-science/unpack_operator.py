# Unpack Operator

""" *args : name 'args' is not necessary but it's a standard practice"""

# Accept any number of arguments from the type of list
def get_sum(*list):
    value = 0
    for sale in list:
        print(sale)
        value += sum(sale)
    return value

a_sale = [10,100,20,147]
b_sale = [-190,4,5,6,45]
c_sale = [11,22]

a_sum = get_sum(a_sale)
print(a_sum)
ab_sum = get_sum(a_sale,b_sale)
print(ab_sum)
total_sum = get_sum(a_sale,b_sale,c_sale)
print(total_sum)

""" **kwargs :   unpacking operator for dictionary
                 name 'kwargs' is not necessary but it's a standard practice
"""

def kwarg_func(**kargs):
    for key,value in kargs.items():
        print(key, ":",value)

kwarg_func(Head="Brian",assistant="Smith")

