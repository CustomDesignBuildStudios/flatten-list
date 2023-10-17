def flatten_list(lst):
    arr = []
    for item in lst:
        if isinstance(item, list):
            arr.extend(flatten_list(item))
        else:
            arr.append(item)
    return arr

print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))

