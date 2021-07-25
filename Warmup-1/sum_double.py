'''
About the problem:

Given two int values, return their sum. Unless the two values are the same, then return double their sum.

Examples:
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double_v1(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return (a + b)

def sum_double_v2(a, b):
    sum = a + b
    if a == b:
        sum *= 2
    return sum

def sum_double_v3(a, b):
    return (a + b) * (2 if a == b else 1)

def sum_double_v4(a, b):
    return (a + b) * (a == b and 2 or 1)

# Problem: https://codingbat.com/prob/p141905
