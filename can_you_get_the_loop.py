"""def loop_size(node):
    flag = True
    arr = node
    result = []
    while flag:
        result.append(arr)
        arr = arr.next
        if arr in result:
            flag = False
            loop_size = len(result) - result.index(arr.next) + 1
    if loop_size == 2:
        return loop_size - 1
    else:
        return loop_size"""


def loop_size(node):
    my_dict = dict()
    current_element = node
    i = 0
    while current_element not in my_dict:
        my_dict[current_element] = i
        current_element = current_element.next
        i += 1
    size = i - my_dict.get(current_element)
    return size