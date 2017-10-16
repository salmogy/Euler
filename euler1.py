def sum_multiples(n):
    items = [x for x in range(n) if (x % 5 == 0) or (x % 3 == 0)]
    return items
print sum_multiples(1000)