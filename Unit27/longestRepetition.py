# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(elements):
    counts = {k:1 for k in set(elements)}
    for i in range(1,len(elements)):
        counts[elements[i]] = counts[elements[i]] + 1 if elements[i] == elements[i-1] else 1
    return  max(counts, key=counts.get) if elements else None





#For example,

print (longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print (longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print (longest_repetition([1,2,3,4,5]))
# 1

print (longest_repetition([]))
# None

