def second_smallest(numbers):
    a1, a = float('inf'), float('inf')
    for x1 in numbers:
        if x1 <= a1:
            a1, a = x1, a
        elif x1 < a:
            a = x1
    return a
print(second_smallest([1, 2, -8, -2, 0]))
