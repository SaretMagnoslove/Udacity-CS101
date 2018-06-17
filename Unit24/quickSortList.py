def quickSortList(numbers):
    if not numbers or len(numbers) <= 1: 
        return numbers
    else:
        pivot, lower, higher = numbers[0], [], []
        for number in numbers[1:]:
            if number <= pivot:
                lower.append(number)
            else:
                higher.append(number)
        return quickSortList(lower) + [numbers[0]] + quickSortList(higher) 

print(quickSortList([]))
print(quickSortList([3,5,6,4,3,5,6,7,8,64,3,2,5]))


    