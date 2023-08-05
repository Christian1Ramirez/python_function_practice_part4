# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(number, start, end):
    return start <= number <= end

print(num_within(3, 2, 4))
print(num_within(110, 2, 10))



# The function num_within(n, start, end) knows to return a boolean because of the expression used within the return statement. 
# In Python, comparison operators (such as >=, <=, and in) evaluate to boolean values (True or False).


"""
def num_within(n):
    if n in range(3, 9):
        print(f"{n} is in the range")
    else:
        print("The number is outside the given range.")

num_within(5)
"""


