# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if day == 'Saturday' or day == 'Sunday': return True
    else: return False

# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(value):
    p5, p2, p1 = 0, 0, 0
    while value != 0:
        if value // 5 > 0:
            p5 += 1
            value -= 5
        elif value // 2 > 0:
            p2 += 1
            value -= 2        
        else:
            p1 += 1
            value -= 1  
    return p5, p2, p1

# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a, b, c):
    return max(a, b, c) - min(a, b, c)