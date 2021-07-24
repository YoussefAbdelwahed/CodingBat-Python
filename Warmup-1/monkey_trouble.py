'''
About the problem:

We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# Examples:
monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

# Implementation:

# both monkeys should have the same state, for us to be in trouble, both should be False or True
def monkey_trouble_v1(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    return False

def monkey_trouble_v2(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

def monkey_trouble_v3(a_smile, b_smile):
    return a_smile == b_smile

def monkey_trouble_v4(a_smile, b_smile):
    in_trouble = False
    if a_smile == b_smile:
        in_trouble = True
    return in_trouble

# Always use mnmonic variables names even if it will be too long 
# it makes code self documenting and easier to understand

# One of python's conventions is to leave a line between function like what we did above.


# Problem : https://codingbat.com/prob/p120546