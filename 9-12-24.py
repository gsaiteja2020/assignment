'''
1.Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)
'''
def flatten(nested_tuple):
    flat_tuple = ()
    for item in nested_tuple:
        if isinstance(item, tuple):
            flat_tuple += flatten(item) 
        else:
            flat_tuple += (item,)  
    return flat_tuple

t = (1, (2, 3), (4, 5, 6))
flattened_tuple = flatten(t)
print(flattened_tuple)

'''
2.Write a Python program to sort a tuple of tuples based on the second element
of each tuple.
Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))
'''
def sorting(input_tuple):
    
    tuple_list = list(input_tuple)
    n = len(tuple_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tuple_list[j][1] > tuple_list[j + 1][1]:
                tuple_list[j], tuple_list[j + 1] = tuple_list[j + 1], tuple_list[j]
    
    return tuple(tuple_list)

t = ((1, 2), (3, 1), (5, 0))
sorted = sorting(t)
print(sorted)


