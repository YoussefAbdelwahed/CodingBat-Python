'''
About the problem:

The parameter weekday is True if it is a weekday, and the parameter vacation is True
if we are on vacation. We sleep in if it is not a weekday or we're on vacation.Return True if we sleep in.

# Examples:
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in_v1(weekday, vacation):
    if not weekday or vacation:
        return True
    return False

def sleep_in_v2(weekday, vacation):
    return not weekday or vacation

# Remember that the order of the booleans operators is the following: (not, and, or).
# As an example: if passed Arguments were sleep_in(True, True):

# The boolean expression will be evaluated in this order: not True or True
#                                                           False or True
#                                                                True



# The problem link: https://codingbat.com/prob/p173401
