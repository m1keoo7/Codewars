def sort_array(source_array):
    a = [i for i in source_array if i % 2 != 0]
    a.sort()
    for index, elem in enumerate(source_array):
        if elem % 2 == 0:
            a.insert(index, elem)
    return a


print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([7, 1]))