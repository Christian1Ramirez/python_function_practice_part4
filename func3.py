# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    return string[::-1]

string = "redrum"
    
print(rev_string(string))

"""
for my notes:

[::-1] is a slicing operation that works as follows:
The first colon : specifies the starting index of the slice. Leaving it empty means the slice starts from the beginning of the string.
The second colon : specifies the ending index of the slice. Leaving it empty means the slice goes to the end of the string.
The -1 specifies the step, which in this case is -1, meaning that the slice goes through the string from end to beginning, effectively reversing it.
"""

# Here's what the -1 step value does:
# Direction: A positive step value would move from left to right through the string, taking characters in the usual forward order. A step value of -1, however, goes in the opposite direction, moving from right to left.
# Increment: The absolute value of the step determines the increment between indices. A step value of 1 or -1 means you're taking every character, but the sign determines the direction. A step value of -1 means you're taking every character in the reverse order.
# Starting and Ending Points: Since the step is -1, the slice starts at the end of the string (if no start value is provided) and ends at the beginning of the string (if no stop value is provided).