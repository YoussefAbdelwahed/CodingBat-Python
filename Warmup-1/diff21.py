'''
About the problem:

Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.

Examples:

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''

# We can use the built-in function abs to get the absolute value of a number
# But I liked to remind you of what is the absolute value of a number check the code below

def get_abs(n):
    # tha absolute val of a number is n if n >= 0 and -n if n < 0, two possible cases
    # And the abs value of any number is the difference between the number and Zero
    return n if n >= 0 else -n

def diff21_v1(n):
    if n > 21:
        return get_abs(n - 21) * 2
    else:
        return get_abs(n - 21)

def diff21_v2(n):
    diff = get_abs(n - 21)
    if n > 21:
        diff *= 2
    return  diff

def diff21_v3(n):
    return get_abs(n - 21) * (2 if n > 21 else 1)

def diff21_v4(n):
    return get_abs(n - 21) * (n > 21 and 2 or 1)

# Problem: https://codingbat.com/prob/p197466