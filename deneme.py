def sum_all(*values):
    total = 0 
    for value in values:
        total = total + value
    return total
sum_all(2,3,4,2,2,3,4,5)