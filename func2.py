# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(*arg):
    result = 1
    for number in arg:
        result *= number
    return result

a = 1
b = 2
c = 3

print(mult_list(a, b, c))
