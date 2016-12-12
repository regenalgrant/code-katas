def find_outlier(integer):
    odd = [i for i in integer if i % 2 != 0]
    even = [i for i in integer if i % 2 == 0]
    return odd[0] if len(odd) < len(even) else even[0]