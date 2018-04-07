def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x1 in numbers:
        if x1 <= a1:
            a1, a2 = x1, a1
        elif x1 < a2:
            a2 = x1
    return a2
print(second_smallest([1, 2, -8, -2, 0]))
