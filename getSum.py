def get_sum(a,b):
    if a == b:
        return a
    sum = 0
    for num in range(min(a,b), max(a,b)+1):
        sum += num
    return sum
    